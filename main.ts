// main.ts — entrypoint for the post-x-promote-make-your-own-bounty-01 bounty.
//
// What this program does, nothing more: it reads POST.json from the same
// directory as this file and copies it into the output directory, so the
// house can read the address of the X post this entry hands in.
//
// It uses only the Node.js standard library, needs no network, and takes no
// arguments. The output directory comes from MAKEFUN_OUTPUT_DIR when that
// variable is set, and defaults to /output otherwise.

import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "POST.json");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "POST.json");

if (!existsSync(source)) {
  console.error(`POST.json not found next to main.ts (looked in ${here})`);
  process.exit(1);
}

// Validate that the file is a JSON object with a url string before copying,
// so a malformed POST.json fails loudly here instead of downstream. The url
// is the post's address as X shows it: https://x.com/<handle>/status/<id>.
const parsed = JSON.parse(readFileSync(source, "utf8"));
if (typeof parsed !== "object" || parsed === null || Array.isArray(parsed)) {
  console.error("POST.json must hold a single JSON object");
  process.exit(1);
}
if (typeof parsed.url !== "string" || parsed.url.length === 0) {
  console.error('POST.json must hold a "url" string naming the X post');
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
console.log(`Wrote ${target} (${parsed.url})`);
