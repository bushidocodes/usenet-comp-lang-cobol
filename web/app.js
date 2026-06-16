/* ============================================================
   COBOL.NEWS — Vanilla JS SPA
   ============================================================ */

"use strict";

// ============================================================
// Constants
// ============================================================

const PAGE_SIZE = 50;
const DATA = "data";

// ============================================================
// State
// ============================================================

const state = {
  feedData: [],     // current list of thread cards
  feedPage: 0,      // pages already rendered
  feedSort: "hot",  // for load-more continuity
};

// JSON fetch cache
const cache = Object.create(null);

// ============================================================
// DOM helpers
// ============================================================

function $(id) { return document.getElementById(id); }

function esc(s) {
  return String(s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function fmt(n) { return Number(n).toLocaleString(); }

function fmtK(n) {
  if (n >= 10000) return Math.round(n / 1000) + "k";
  if (n >= 1000)  return (n / 1000).toFixed(1) + "k";
  return String(n);
}

function fmtDate(iso) {
  if (!iso) return "";
  try {
    const d = new Date(iso);
    if (isNaN(d)) return iso.slice(0, 10);
    return d.toLocaleDateString("en-US", { year: "numeric", month: "short", day: "numeric" });
  } catch { return iso.slice(0, 10); }
}

function enc(s) { return encodeURIComponent(s ?? ""); }

// ============================================================
// Data loading
// ============================================================

async function load(url) {
  if (!cache[url]) {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`${res.status} ${url}`);
    cache[url] = await res.json();
  }
  return cache[url];
}

// ============================================================
// Router
// ============================================================

function parseHash() {
  const raw = location.hash.replace(/^#\/?/, "") || "";
  const [pathPart = "", queryPart = ""] = raw.split("?");
  const segs = pathPart.split("/").filter(Boolean);
  const params = new URLSearchParams(queryPart);
  return { segs, params };
}

function navigate(path) {
  location.hash = "/" + path;
}
window.navigate = navigate;   // used by inline onclick handlers

async function route() {
  const { segs, params } = parseHash();
  const [first, second] = segs;

  updateSidebarActive(first, second);

  try {
    switch (first) {
      case undefined:
      case "":       return renderFeed("hot");
      case "new":    return renderFeed("new");
      case "popular":return renderFeed("popular");
      case "thread": return renderThread(second);
      case "year":   return renderYear(second);
      case "topic":  return renderTopic(second);
      case "authors":return renderAuthors();
      case "stats":  return renderStats();
      case "search": return renderSearch(params.get("q") || "");
      case "author": return renderAuthor(second);
      default:       return renderFeed("hot");
    }
  } catch (err) {
    if (err.message && err.message.includes("404")) {
      showDataMissing();
    } else {
      $("content").innerHTML = `<div class="error-box">Error: ${esc(err.message)}</div>`;
    }
  }
}

function showDataMissing() {
  $("content").innerHTML = `
    <div class="data-missing">
      <h2>Data not generated yet</h2>
      <p>Run the export script first to build the static JSON files:</p>
      <br>
      <code>python export_json.py</code>
      <br><br>
      <p>This takes a few minutes and only needs to run once.</p>
    </div>`;
}

// ============================================================
// Sidebar init
// ============================================================

async function initSidebar() {
  try {
    const idx = await load(`${DATA}/index.json`);

    const yearNav = $("year-nav");
    yearNav.innerHTML = idx.years.slice().reverse().map(y =>
      `<a href="#/year/${y.year}" class="nav-link" data-route="year-${y.year}">`
      + esc(y.year)
      + `<span>${fmt(y.threads)}</span></a>`
    ).join("");

    const topicNav = $("topic-nav");
    topicNav.innerHTML = idx.topics
      .filter(t => t.threads > 0)
      .map(t =>
        `<a href="#/topic/${t.slug}" class="nav-link" data-route="topic-${t.slug}">`
        + esc(t.name)
        + `<span>${fmt(t.threads)}</span></a>`
      ).join("");
  } catch {
    // If data isn't exported yet, sidebar stays as "Loading…"
  }
}

function updateSidebarActive(first, second) {
  document.querySelectorAll(".nav-link").forEach(el => el.classList.remove("active"));
  let key = first || "hot";
  if (first === "year")  key = `year-${second}`;
  if (first === "topic") key = `topic-${second}`;
  const active = document.querySelector(`.nav-link[data-route="${key}"]`);
  if (active) active.classList.add("active");
}

// ============================================================
// Thread card
// ============================================================

function threadCard(t) {
  const topicChips = (t.t || []).map(([name, slug]) =>
    `<a href="#/topic/${slug}" class="chip" onclick="event.stopPropagation()">${esc(name)}</a>`
  ).join("");

  const authorHtml = t.by
    ? `<a href="#/author/${enc(t.em)}" class="author-link" onclick="event.stopPropagation()">${esc(t.by)}</a><span class="sep">·</span>`
    : "";

  return `
<article class="thread-card" onclick="navigate('thread/${t.a}')">
  <div class="score">
    <span class="score-num">${fmtK(t.c)}</span>
    <span class="score-label">msg${t.c !== 1 ? "s" : ""}</span>
  </div>
  <div class="thread-info">
    <h2 class="thread-title">
      <a href="#/thread/${t.a}" onclick="event.stopPropagation()">${esc(t.s)}</a>
    </h2>
    <div class="thread-meta">
      ${authorHtml}
      <span class="date">${esc(t.sp)}</span>
      <span class="sep">·</span>
      <span>${t.p} participant${t.p !== 1 ? "s" : ""}</span>
    </div>
    ${topicChips ? `<div class="chips">${topicChips}</div>` : ""}
  </div>
</article>`;
}

// ============================================================
// Feed view (hot / new / popular)
// ============================================================

async function renderFeed(sort) {
  setContent(`<div class="loading"><div class="loading-spinner"></div><p>Loading…</p></div>`);

  const filename = sort === "new" ? "new.json" : "hot.json";
  let data = await load(`${DATA}/${filename}`);

  if (sort === "popular") {
    data = [...data].sort((a, b) => b.p - a.p);
  }

  state.feedData = data;
  state.feedPage = 0;
  state.feedSort = sort;

  const countLabel = `${fmt(data.length)} threads`;
  const tabs = ["hot", "new", "popular"].map(s => {
    const href = s === "hot" ? "#/" : `#/${s}`;
    const label = s === "popular" ? "Most Discussed" : s.charAt(0).toUpperCase() + s.slice(1);
    return `<a href="${href}" class="sort-tab ${s === sort ? "active" : ""}">${label}</a>`;
  }).join("");

  setContent(`
    <div class="feed-header">
      <div class="sort-tabs">${tabs}</div>
      <span class="feed-count">${countLabel}</span>
    </div>
    <div id="thread-list"></div>
  `);

  appendFeedPage();
}

function appendFeedPage() {
  const list = $("thread-list");
  if (!list) return;

  const start = state.feedPage * PAGE_SIZE;
  const slice = state.feedData.slice(start, start + PAGE_SIZE);
  state.feedPage++;

  list.insertAdjacentHTML("beforeend", slice.map(threadCard).join(""));

  // Remove old load-more
  const oldBtn = document.querySelector(".load-more");
  if (oldBtn) oldBtn.remove();

  const remaining = state.feedData.length - state.feedPage * PAGE_SIZE;
  if (remaining > 0) {
    const btn = document.createElement("button");
    btn.className = "load-more";
    btn.textContent = `Load ${Math.min(PAGE_SIZE, remaining)} more (${fmt(remaining)} remaining)`;
    btn.onclick = appendFeedPage;
    $("content").appendChild(btn);
  }
}

// ============================================================
// Year view
// ============================================================

async function renderYear(year) {
  setContent(`<div class="loading"><div class="loading-spinner"></div></div>`);
  const data = await load(`${DATA}/year/${year}.json`);

  state.feedData = data;
  state.feedPage = 0;
  state.feedSort = "hot";

  setContent(`
    <h2 class="view-title">${esc(year)} <span class="muted">— ${fmt(data.length)} threads</span></h2>
    <div id="thread-list"></div>
  `);
  appendFeedPage();
}

// ============================================================
// Topic view
// ============================================================

async function renderTopic(slug) {
  setContent(`<div class="loading"><div class="loading-spinner"></div></div>`);
  const [data, idx] = await Promise.all([
    load(`${DATA}/topic/${slug}.json`),
    load(`${DATA}/index.json`),
  ]);

  const topicInfo = idx.topics.find(t => t.slug === slug);
  const title = topicInfo ? topicInfo.name : slug;

  state.feedData = data;
  state.feedPage = 0;
  state.feedSort = "hot";

  setContent(`
    <h2 class="view-title">${esc(title)} <span class="muted">— ${fmt(data.length)} threads</span></h2>
    <div id="thread-list"></div>
  `);
  appendFeedPage();
}

// ============================================================
// Thread reader
// ============================================================

async function renderThread(anchor) {
  setContent(`<div class="loading"><div class="loading-spinner"></div><p>Loading thread…</p></div>`);

  const thread = await load(`${DATA}/threads/${anchor}.json`);
  const topicChips = (thread.topics || []).map(([name, slug]) =>
    `<a href="#/topic/${slug}" class="chip">${esc(name)}</a>`
  ).join("");

  const msgHtml = thread.messages.map((msg, i) => messageCard(msg, thread.subject, i)).join("");

  setContent(`
    <a href="#/" class="back-btn">← Back</a>
    <div class="thread-header">
      <h1>${esc(thread.subject)}</h1>
      <div class="thread-stats">
        <span>${fmt(thread.count)} message${thread.count !== 1 ? "s" : ""}</span>
        <span class="sep">·</span>
        <span>${fmt(thread.participants)} participant${thread.participants !== 1 ? "s" : ""}</span>
        <span class="sep">·</span>
        <span>${esc(thread.span)}</span>
      </div>
      ${topicChips ? `<div class="chips" style="margin-top:.5rem">${topicChips}</div>` : ""}
    </div>
    <div class="messages" id="message-list">
      ${msgHtml}
    </div>
  `);
}

function messageCard(msg, threadSubject, idx) {
  const depth = Math.min(msg.dep ?? 0, 5);
  const indent = depth * 20;
  const isDifferentSubject = msg.s && msg.s !== threadSubject;

  const lines = (msg.body ?? "").split("\n");
  const isLong = lines.length > 35;
  const collapseId = `body-${idx}`;
  const btnId = `btn-${idx}`;

  const bodyHtml = lines.map(line => {
    const trimmed = line.trimStart();
    if (trimmed.startsWith(">") || trimmed.startsWith("|") || trimmed.startsWith("›")) {
      return `<span class="quoted">${esc(line)}</span>`;
    }
    return esc(line);
  }).join("\n");

  const authorId = msg.em ? enc(msg.em) : "";

  return `
<div class="message depth-${depth}" style="margin-left:${indent}px">
  <div class="msg-header">
    ${msg.em
      ? `<a href="#/author/${authorId}" class="msg-author">${esc(msg.by || msg.em)}</a>`
      : `<span class="msg-author">${esc(msg.by || "unknown")}</span>`
    }
    <span class="msg-date">${fmtDate(msg.d)}</span>
  </div>
  ${isDifferentSubject ? `<div class="msg-subject">${esc(msg.s)}</div>` : ""}
  <pre class="msg-body${isLong ? "" : " expanded"}" id="${collapseId}">${bodyHtml}</pre>
  ${isLong ? `<button class="expand-btn" id="${btnId}" onclick="toggleBody('${collapseId}','${btnId}')">▼ Show full message (${lines.length} lines)</button>` : ""}
</div>`;
}

function toggleBody(bodyId, btnId) {
  const pre = $(bodyId);
  const btn = $(btnId);
  if (!pre) return;
  if (pre.classList.contains("expanded")) {
    pre.classList.remove("expanded");
    btn.textContent = `▼ Show full message`;
  } else {
    pre.classList.add("expanded");
    btn.textContent = "▲ Collapse";
  }
}
window.toggleBody = toggleBody;

// ============================================================
// Authors list
// ============================================================

async function renderAuthors() {
  setContent(`<div class="loading"><div class="loading-spinner"></div></div>`);
  const authors = await load(`${DATA}/authors.json`);

  const rows = authors.map((a, i) => `
    <tr>
      <td class="rank">${i + 1}</td>
      <td><a href="#/author/${a.id}">${esc(a.name || a.email)}</a></td>
      <td class="email">${esc(a.email)}</td>
      <td class="num">${fmt(a.messages)}</td>
      <td class="num">${fmt(a.threads)}</td>
    </tr>`).join("");

  setContent(`
    <h2 class="view-title">Top Contributors <span class="muted">— ${fmt(authors.length)} shown</span></h2>
    <table class="authors-table">
      <thead>
        <tr>
          <th>#</th><th>Name</th><th>Email</th><th>Messages</th><th>Threads</th>
        </tr>
      </thead>
      <tbody>${rows}</tbody>
    </table>`);
}

// ============================================================
// Author profile
// ============================================================

async function renderAuthor(authorId) {
  setContent(`<div class="loading"><div class="loading-spinner"></div></div>`);

  let author;
  try {
    author = await load(`${DATA}/author/${authorId}.json`);
  } catch {
    // Not in top-500: fall back to authors list
    const authors = await load(`${DATA}/authors.json`);
    author = authors.find(a => a.id === authorId);
    if (!author) {
      setContent(`<div class="empty-state"><p>Author not found.</p></div>`);
      return;
    }
    author.threads = [];
    author.thread_count = author.threads_count ?? "—";
  }

  state.feedData = author.threads || [];
  state.feedPage = 0;
  state.feedSort = "hot";

  setContent(`
    <a href="#/authors" class="back-btn">← All authors</a>
    <div class="author-header">
      <div class="author-name-big">${esc(author.name || author.email)}</div>
      <div class="author-email-small">${esc(author.email)}</div>
      <div class="author-stats">
        <div class="author-stat">
          <div class="author-stat-num">${fmt(author.messages)}</div>
          <div class="author-stat-label">Messages</div>
        </div>
        <div class="author-stat">
          <div class="author-stat-num">${fmt(author.thread_count ?? (author.threads || []).length)}</div>
          <div class="author-stat-label">Threads</div>
        </div>
      </div>
    </div>
    <h3 style="margin-bottom:.75rem;color:var(--text-muted);font-size:.85rem;font-weight:600;text-transform:uppercase;letter-spacing:.07em">Top Threads</h3>
    <div id="thread-list"></div>
  `);

  if (state.feedData.length === 0) {
    $("thread-list").innerHTML = `<div class="empty-state"><p>No thread data available for this author.</p></div>`;
  } else {
    appendFeedPage();
  }
}

// ============================================================
// Stats page
// ============================================================

async function renderStats() {
  setContent(`<div class="loading"><div class="loading-spinner"></div></div>`);
  const idx = await load(`${DATA}/index.json`);

  const maxMsgs = Math.max(...idx.years.map(y => y.messages), 1);

  const yearBars = idx.years.map(y => {
    const pct = (y.messages / maxMsgs * 100).toFixed(1);
    return `
      <div class="stat-bar-row" onclick="navigate('year/${y.year}')" title="${y.year}: ${fmt(y.messages)} messages, ${fmt(y.threads)} threads">
        <span class="bar-label">${y.year}</span>
        <div class="bar-track"><div class="bar-fill" style="width:${pct}%"></div></div>
        <span class="bar-val">${fmt(y.messages)}</span>
      </div>`;
  }).join("");

  const topicCards = idx.topics
    .filter(t => t.threads > 0)
    .map(t => `
      <a href="#/topic/${t.slug}" class="topic-card">
        <div class="topic-name">${esc(t.name)}</div>
        <div class="topic-count">${fmt(t.threads)} threads · ${fmt(t.messages)} msgs</div>
      </a>`).join("");

  setContent(`
    <div class="stats-view">
      <h2>Archive Statistics</h2>
      <div class="stat-cards">
        <div class="stat-card">
          <div class="stat-num">${fmt(idx.messages)}</div>
          <div class="stat-label">Total Messages</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">${fmt(idx.threads)}</div>
          <div class="stat-label">Threads</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">${fmt(idx.authors)}</div>
          <div class="stat-label">Unique Authors</div>
        </div>
        <div class="stat-card">
          <div class="stat-num">${idx.date_start}–${idx.date_end}</div>
          <div class="stat-label">Date Range</div>
        </div>
      </div>

      <h3>Messages per Year</h3>
      <div class="stat-bars">${yearBars}</div>

      <h3>Topics</h3>
      <div class="topic-grid">${topicCards}</div>
    </div>`);
}

// ============================================================
// Search
// ============================================================

// Split a string into lowercase alphanumeric search tokens.
function searchTokens(s) {
  return (s.toLowerCase().match(/[a-z0-9]+/g) || []);
}

// Score one thread against the query terms. Every term must appear in the
// subject or the snippet (AND); whole-word and subject hits rank above
// substring and snippet-only hits. Returns -1 if any term is missing.
function searchScore(subjTokens, snipTokens, terms) {
  let total = 0;
  for (const t of terms) {
    let s = 0;
    if (subjTokens.includes(t)) s = 10;
    else if (snipTokens.includes(t)) s = 3;
    else if (subjTokens.some(w => w.includes(t))) s = 6;     // substring in subject
    else if (snipTokens.some(w => w.includes(t))) s = 1;     // substring in snippet
    if (s === 0) return -1;
    total += s;
  }
  return total;
}

async function renderSearch(query) {
  if (!query.trim()) { renderFeed("hot"); return; }

  setContent(`<div class="loading"><div class="loading-spinner"></div><p>Searching…</p></div>`);

  // hot.json gives full cards (subject + metadata); search.json gives the
  // first-post snippet per anchor so search reaches body content, not just
  // subjects. Both are cached after first load.
  const [hot, snippets] = await Promise.all([
    load(`${DATA}/hot.json`),
    load(`${DATA}/search.json`).catch(() => ({})),  // tolerate older exports
  ]);

  const terms = searchTokens(query);
  const scored = [];
  for (const t of hot) {
    const sc = searchScore(searchTokens(t.s), searchTokens(snippets[t.a] || ""), terms);
    if (sc >= 0) scored.push([sc, t]);
  }
  scored.sort((a, b) => b[0] - a[0] || b[1].c - a[1].c);
  const results = scored.map(x => x[1]);

  state.feedData = results;
  state.feedPage = 0;
  state.feedSort = "hot";

  setContent(`
    <h2 class="view-title">
      Search: &ldquo;${esc(query)}&rdquo;
      <span class="muted">— ${fmt(results.length)} thread${results.length !== 1 ? "s" : ""}</span>
    </h2>
    ${results.length === 0
      ? `<div class="empty-state"><p>No threads matched your search.</p></div>`
      : `<div id="thread-list"></div>`
    }`);

  if (results.length > 0) appendFeedPage();
}

// ============================================================
// Search form
// ============================================================

$("search-form").addEventListener("submit", e => {
  e.preventDefault();
  const q = $("search-input").value.trim();
  if (q) location.hash = `/search?q=${enc(q)}`;
});

// Keep search input in sync with URL when navigating
function syncSearchInput() {
  const { segs, params } = parseHash();
  const input = $("search-input");
  if (segs[0] === "search") {
    input.value = params.get("q") || "";
  } else {
    input.value = "";
  }
}

// ============================================================
// Content helper
// ============================================================

function setContent(html) {
  $("content").innerHTML = html;
  window.scrollTo(0, 0);
}

// ============================================================
// Boot
// ============================================================

window.addEventListener("hashchange", () => { syncSearchInput(); route(); });
window.addEventListener("DOMContentLoaded", () => {
  initSidebar();
  syncSearchInput();
  route();
});
