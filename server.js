#!/usr/bin/env node
/**
 * Static file server for COBOL.NEWS.
 * Zero npm dependencies — uses only Node.js built-ins.
 *
 * Usage:  node server.js [port]
 *         Default port: 3000
 */

const http = require("http");
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");

const PORT = Number(process.env.PORT) || Number(process.argv[2]) || 3000;
const WEB_DIR = path.join(__dirname, "web");

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".ico": "image/x-icon",
  ".png": "image/png",
  ".svg": "image/svg+xml",
};

function serveIndex(res) {
  const indexPath = path.join(WEB_DIR, "index.html");
  fs.readFile(indexPath, (err, data) => {
    if (err) { res.writeHead(500); res.end("Internal error"); return; }
    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-cache" });
    res.end(data);
  });
}

function serveFile(req, res, filePath) {
  const ext = path.extname(filePath).toLowerCase();
  const mime = MIME[ext] || "application/octet-stream";

  // Thread JSON files are stable — allow short caching
  const isData = filePath.includes(path.sep + "data" + path.sep);
  const cacheControl = isData ? "public, max-age=300" : "no-cache";

  // Gzip if client accepts it and file is text
  const acceptsGzip = (req.headers["accept-encoding"] || "").includes("gzip");
  const isText = mime.startsWith("text") || mime.includes("json") || mime.includes("javascript");

  fs.readFile(filePath, (err, data) => {
    if (err) { serveIndex(res); return; }  // SPA fallback

    if (acceptsGzip && isText) {
      zlib.gzip(data, (err2, compressed) => {
        if (err2) {
          res.writeHead(200, { "Content-Type": mime, "Cache-Control": cacheControl });
          res.end(data);
        } else {
          res.writeHead(200, {
            "Content-Type": mime,
            "Content-Encoding": "gzip",
            "Cache-Control": cacheControl,
          });
          res.end(compressed);
        }
      });
    } else {
      res.writeHead(200, { "Content-Type": mime, "Cache-Control": cacheControl });
      res.end(data);
    }
  });
}

const server = http.createServer((req, res) => {
  if (req.method !== "GET" && req.method !== "HEAD") {
    res.writeHead(405); res.end("Method not allowed"); return;
  }

  const urlPath = req.url.split("?")[0].replace(/\/+$/, "") || "/";
  const filePath = path.join(WEB_DIR, urlPath);

  // Prevent directory traversal
  if (!filePath.startsWith(WEB_DIR)) {
    res.writeHead(403); res.end("Forbidden"); return;
  }

  fs.stat(filePath, (err, stat) => {
    if (!err && stat.isFile()) {
      serveFile(req, res, filePath);
    } else if (!err && stat.isDirectory()) {
      serveFile(req, res, path.join(filePath, "index.html"));
    } else {
      // Unknown path — serve SPA shell (index.html handles routing)
      serveIndex(res);
    }
  });
});

server.listen(PORT, "0.0.0.0", () => {
  console.log(`\n  COBOL.NEWS  →  http://localhost:${PORT}\n`);
  console.log("  Press Ctrl+C to stop.\n");
});
