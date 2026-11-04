const D = __DATA__;
const CORE = ["ETH 101", "REC 101", "SEC 101", "COM 101"];
const CATC = { "4.A.1": "#7fa7d9", "4.A.2": "#d0a2e0", "4.A.3": "#e3b27a", "4.A.4": "#8fc29a" };
const CATN = { "4.A.1": "Taking in information", "4.A.2": "Thinking it through", "4.A.3": "Doing the work", "4.A.4": "Working with people" };
const GOLD = "#e3c46a", ROLE = "#e9e4cf", HALL = "#a6ead9", LIT = "#64a79c";
const DOES = { reads: "reads and reports", creates: "creates and drafts", changes: "changes existing things", "moves-money": "moves money or binds the company", physical: "acts in the physical world", directs: "directs other agents" };

// ---- which skills light which requirement nodes
const SK = {}; D.skills.forEach(s => SK[s.n] = s);
const litBy = {};
D.skills.forEach(s => s.dwas.forEach(i => (litBy[i] ||= []).push(s)));
const needCount = new Array(D.dwas.length).fill(0);
D.occs.forEach(o => o[2].forEach(i => needCount[i]++));
const isHall = s => s.status === "accredited";
const isEng = s => !isHall(s) && (s.eh || []).length > 0; // Hallmarked for an engine size (METHOD_V4.md)
const ENG = "#9fd8f0";
const ENGN = { "gpt-5.4-nano": "GPT-5.4 nano", "claude-haiku-5-5": "Haiku 5.5", "claude-sonnet-5-5": "Sonnet 5.5", "gpt-5.5": "GPT-5.5" };
const SMALL = new Set(["gpt-5.4-nano", "claude-haiku-5-5"]);
const engWord = s => `Hallmarked for ${(s.eh || []).some(e => SMALL.has(e)) ? "small" : "frontier"} engines (${(s.eh || []).map(e => ENGN[e] || e).join(", ")})`;
const keyOf = {}; D.keys.forEach(k => k.courses.forEach(c => (keyOf[c] ||= []).push(k)));

// ---- layout: O*NET regions as constellations around the core (unchanged from v1)
const iwaMembers = D.iwas.map(() => []);
D.dwas.forEach((d, i) => iwaMembers[d[1]].push(i));
const gwaIwas = D.gwas.map(() => []); D.iwas.forEach((w, i) => gwaIwas[w[2]].push(i));
const cats = Object.keys(CATN);
const pos = new Array(D.dwas.length), iwaPos = [], gwaPos = [];
const GAP = 7;
function packAround(items) {
  const placed = [];
  items.forEach(it => {
    if (!placed.length) { it.x = 0; it.y = 0; placed.push(it); return; }
    for (let t = 0; t < 4000; t++) {
      const th = t * 0.35, rr = 3 * th, x = rr * Math.cos(th), y = rr * Math.sin(th);
      if (placed.every(p => Math.hypot(p.x - x, p.y - y) >= p.r + it.r + GAP)) { it.x = x; it.y = y; placed.push(it); return; }
    }
    it.x = 0; it.y = 0; placed.push(it);
  });
}
const blobs = D.gwas.map((g, gi) => {
  const cl = gwaIwas[gi].map(ii => ({ ii, r: 8.5 * Math.sqrt(iwaMembers[ii].length) + 7 })).sort((x, y) => y.r - x.r);
  packAround(cl);
  return { gi, cl, r: Math.max(...cl.map(c => Math.hypot(c.x, c.y) + c.r)) + 10 };
});
const order = []; cats.forEach(c => D.gwas.forEach((g, gi) => { if (g[0].startsWith(c)) order.push(gi); }));
const totalR = order.reduce((t, gi) => t + blobs[gi].r, 0);
let acc = -135; const placedB = [{ x: 0, y: 0, r: 190 }];
order.forEach(gi => {
  const b = blobs[gi], w = 360 * b.r / totalR, ang = acc + w / 2; acc += w;
  let r = 300 + b.r;
  for (;;) { const p = polar(ang, r); if (placedB.every(q => Math.hypot(q.x - p.x, q.y - p.y) >= q.r + b.r + 34)) { b.x = p.x; b.y = p.y; break; } r += 8; }
  placedB.push(b); gwaPos[gi] = { x: b.x, y: b.y, r: b.r };
  b.cl.forEach(c => { iwaPos[c.ii] = { x: b.x + c.x, y: b.y + c.y, r: c.r }; });
});
const EXT0 = Math.max(...placedB.map(b => Math.hypot(b.x, b.y) + b.r));
iwaMembers.forEach((mm, ii) => mm.forEach((di, k) => {
  const c = iwaPos[ii], t = k * 2.39996, rr = 8.5 * Math.sqrt(k + 0.6);
  pos[di] = { x: c.x + rr * Math.cos(t), y: c.y + rr * Math.sin(t) };
}));
function polar(deg, r) { const t = (deg - 90) * Math.PI / 180; return { x: r * Math.cos(t), y: r * Math.sin(t) }; }
const catOf = gi => D.gwas[gi][0].slice(0, 5);
const dwaGwa = i => D.iwas[D.dwas[i][1]][2];
const mean = ps => ({ x: ps.reduce((t, p) => t + p.x, 0) / ps.length, y: ps.reduce((t, p) => t + p.y, 0) / ps.length });

// ---- the notables: each skill is a big named node beside the requirements it covers
const NP = {};
CORE.forEach((n, i) => NP[n] = i === 0 ? { x: 0, y: 0 } : polar(-90 + (i - 1) * 120, 78));
const outer = D.skills.filter(s => !CORE.includes(s.n));
outer.forEach(s => {
  const c = mean(s.dwas.map(i => pos[i])), d = Math.hypot(c.x, c.y) || 1;
  NP[s.n] = { x: c.x + c.x / d * 34, y: c.y + c.y / d * 34, ax: c.x, ay: c.y };
});
// keystones sit just outside the skills they bind together
const KP = D.keys.map(k => {
  const top = k.courses.map(n => SK[n]).filter(s => !s.guard).sort((a, b) => b.lvl - a.lvl)[0] || SK[k.courses[0]];
  const c = NP[top.n], d = Math.hypot(c.x, c.y) || 1; return { x: c.x + c.x / d * 110, y: c.y + c.y / d * 110 };
});
// relax: notables and keystones push each other apart, and each is pulled back toward its anchor
const movers = outer.map(s => ({ p: NP[s.n], r: 30, ax: NP[s.n].x, ay: NP[s.n].y })).concat(KP.map(p => ({ p, r: 40, ax: p.x, ay: p.y })));
for (let it = 0; it < 220; it++) {
  for (let a = 0; a < movers.length; a++) for (let b = a + 1; b < movers.length; b++) {
    const A = movers[a].p, B = movers[b].p, dx = B.x - A.x, dy = B.y - A.y, d = Math.hypot(dx, dy) || 0.01, need = movers[a].r + movers[b].r;
    if (d < need) { const f = (need - d) / 2 / d; A.x -= dx * f; A.y -= dy * f; B.x += dx * f; B.y += dy * f; }
  }
  movers.forEach(m => { m.p.x += (m.ax - m.p.x) * 0.02; m.p.y += (m.ay - m.p.y) * 0.02; const d = Math.hypot(m.p.x, m.p.y); if (d < 170) { m.p.x *= 170 / d; m.p.y *= 170 / d; } });
}

// ---- roles: the endgame, as big named landmarks on the rim
const RIM = EXT0 + 120;
const occByCode = {}; D.occs.forEach((o, i) => occByCode[o[0]] = i);
function roleFromLandmark(r) {
  const oi = r.occ ? occByCode[r.occ] : null;
  const need = oi != null ? D.occs[oi][2] : [...new Set(r.courses.flatMap(n => SK[n].dwas))];
  return { name: r.t, build: r.build, cap: r.cap, occ: oi, need, courses: r.courses };
}
const RL = D.roles.map(roleFromLandmark);
function roleSkills(R) { // skills on this role: its own courses, plus any skill that covers one of its requirements
  const set = new Set(R.courses); R.need.forEach(i => (litBy[i] || []).forEach(s => set.add(s.n)));
  return set;
}
function roleAnchor(R) {
  const ps = R.courses.length ? R.courses.map(n => NP[n]) : R.need.map(i => pos[i]);
  const c = mean(ps); return Math.atan2(c.y, c.x);
}
const RP = RL.map(R => ({ a: roleAnchor(R) }));
for (let it = 0; it < 80; it++) RP.forEach((p, i) => RP.forEach((q, j) => { if (i < j) { let d = q.a - p.a; d = Math.atan2(Math.sin(d), Math.cos(d)); if (Math.abs(d) < 0.32) { const f = (0.32 - Math.abs(d)) / 2 * Math.sign(d || 1); p.a -= f; q.a += f; } } }));
RP.forEach(p => { p.x = RIM * Math.cos(p.a); p.y = RIM * Math.sin(p.a); });
const EXT = RIM + 90;

function leaves(cs) { const set = new Set(cs), used = new Set(); cs.forEach(n => SK[n].pre.forEach(p => used.add(p))); return cs.filter(n => NP[n] && !used.has(n)); }
// ---- view
const cv = document.getElementById("map"), ctx = cv.getContext("2d");
const V = { s: 0.2, x: 0, y: 0 }; let W = 0, H = 0, DPR = 1;
let role = null, roleSet = new Set(), roleSk = new Set(), sel = null, tempRP = null;
const MAXS = 40; // 40x the base scale: single requirements read comfortably, with room to spare as the map grows
const fitS = () => Math.min(W, H) / (2 * EXT);
const clampS = v => Math.min(MAXS, Math.max(fitS() * 0.5, v));
function fit() { V.s = fitS(); V.x = W / 2; V.y = H / 2; }
const centerOf = () => ({ x: (W / 2 - V.x) / V.s, y: (H / 2 - V.y) / V.s });
function resize() {
  const r = cv.getBoundingClientRect(); if (!r.width || !r.height) return;
  const c = resize.done ? centerOf() : null, wasFit = resize.done && Math.abs(V.s - fitS()) < 1e-9;
  DPR = window.devicePixelRatio || 1; W = r.width; H = r.height;
  cv.width = Math.round(W * DPR); cv.height = Math.round(H * DPR);
  if (!resize.done || wasFit) { fit(); resize.done = true; } else { V.x = W / 2 - c.x * V.s; V.y = H / 2 - c.y * V.s; }
  miniBg = null; draw();
}
const sx = p => V.x + p.x * V.s, sy = p => V.y + p.y * V.s;
const clampR = (r, lo, hi) => Math.min(hi, Math.max(lo, r));
function poly(X, Y, r, n, rot) { ctx.beginPath(); for (let k = 0; k < n; k++) { const t = rot + k * 2 * Math.PI / n; k ? ctx.lineTo(X + r * Math.cos(t), Y + r * Math.sin(t)) : ctx.moveTo(X + r * Math.cos(t), Y + r * Math.sin(t)); } ctx.closePath(); }
function line(a, b) { ctx.beginPath(); ctx.moveTo(sx(a), sy(a)); ctx.lineTo(sx(b), sy(b)); ctx.stroke(); }
// a travel path: a slight arc, like the curved roads of a passive tree
function road(a, b, bend) {
  const mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2, dx = b.x - a.x, dy = b.y - a.y, k = bend || 0.12;
  ctx.beginPath(); ctx.moveTo(sx(a), sy(a)); ctx.quadraticCurveTo(sx({ x: mx - dy * k, y: my + dx * k }), sy({ x: mx - dy * k, y: my + dx * k }), sx(b), sy(b)); ctx.stroke();
}

function draw() {
  ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  ctx.clearRect(0, 0, W, H);
  const s = V.s, dim = role !== null;
  // rim of roles
  ctx.strokeStyle = "rgba(233,228,207,.07)"; ctx.lineWidth = clampR(26 * s, 1, 40);
  ctx.beginPath(); ctx.arc(sx({ x: 0, y: 0 }), sy({ x: 0, y: 0 }), RIM * s, 0, 6.2832); ctx.stroke();
  // region halos and hub lines
  D.gwas.forEach((g, gi) => {
    const b = gwaPos[gi], col = CATC[catOf(gi)];
    ctx.beginPath(); ctx.arc(sx(b), sy(b), b.r * s, 0, 6.2832); ctx.fillStyle = col + "0d"; ctx.fill();
    ctx.strokeStyle = col + "26"; ctx.lineWidth = clampR(3 * s, 1, 3); line({ x: 0, y: 0 }, b);
    ctx.lineWidth = clampR(1.5 * s, 0.6, 1.6); ctx.strokeStyle = col + "26";
    gwaIwas[gi].forEach(ii => line(b, iwaPos[ii]));
  });
  if (s > 0.6) {
    ctx.strokeStyle = "rgba(140,170,170,.10)"; ctx.lineWidth = 0.8;
    iwaMembers.forEach((mm, ii) => mm.forEach(di => line(iwaPos[ii], pos[di])));
  }
  // requirement nodes (small passives)
  const nr = clampR(2.5 * s, 1.3, 6);
  for (let i = 0; i < D.dwas.length; i++) {
    const p = pos[i], X = sx(p), Y = sy(p);
    if (X < -20 || Y < -20 || X > W + 20 || Y > H + 20) continue;
    const lit = litBy[i], hall = lit && lit.some(isHall), onRole = roleSet.has(i);
    ctx.globalAlpha = dim && !onRole ? 0.3 : 1;
    ctx.beginPath(); ctx.arc(X, Y, lit ? nr * 1.6 : nr, 0, 6.2832);
    ctx.fillStyle = hall ? HALL : lit ? LIT : CATC[catOf(dwaGwa(i))] + (onRole ? "dd" : "5a"); ctx.fill();
    if (onRole) { ctx.strokeStyle = ROLE; ctx.lineWidth = 1.3; ctx.beginPath(); ctx.arc(X, Y, (lit ? nr * 1.6 : nr) + 2.5, 0, 6.2832); ctx.stroke(); }
    if (sel && sel.k === "dwa" && sel.i === i) { ctx.strokeStyle = "#fff"; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(X, Y, nr * 3 + 4, 0, 6.2832); ctx.stroke(); }
  }
  ctx.globalAlpha = 1;
  // spokes: each notable to the requirements it covers
  D.skills.forEach(sk => {
    const on = !dim || roleSk.has(sk.n);
    ctx.strokeStyle = (isHall(sk) ? HALL : LIT) + (on ? "88" : "22"); ctx.lineWidth = clampR(1.6 * s, 0.8, 1.8);
    sk.dwas.forEach(i => line(NP[sk.n], pos[i]));
  });
  // travel paths: prerequisites, the roads between notables
  D.skills.forEach(sk => sk.pre.forEach(p => {
    if (!NP[p] || (CORE.includes(p) && sk.pre.some(q => !CORE.includes(q)))) return;
    const on = dim && roleSk.has(sk.n) && roleSk.has(p);
    ctx.strokeStyle = on ? "rgba(233,228,207,.75)" : dim ? "rgba(233,228,207,.08)" : "rgba(233,228,207,.22)";
    ctx.lineWidth = clampR((on ? 4.5 : 3) * s, on ? 1.6 : 1, on ? 4 : 2.6); road(NP[p], NP[sk.n]);
  }));
  // keystone tethers
  D.keys.forEach((k, ki) => {
    ctx.setLineDash([Math.max(2, 8 * s), Math.max(2, 6 * s)]); ctx.strokeStyle = GOLD + (dim && !k.courses.some(c => roleSk.has(c)) ? "22" : "99"); ctx.lineWidth = clampR(2.4 * s, 1, 2.2);
    k.courses.forEach(c => line(KP[ki], NP[c])); ctx.setLineDash([]);
  });
  // role tethers: from each landmark to its capstone (or to its skills while it has none)
  const rolesNow = RL.map((R, i) => [R, RP[i]]); if (tempRP) rolesNow.push(tempRP);
  rolesNow.forEach(([R, P]) => {
    const active = role && role.name === R.name;
    const to = R.cap && NP[R.cap] ? [R.cap] : leaves(R.courses);
    ctx.strokeStyle = active ? "rgba(233,228,207,.8)" : "rgba(233,228,207,.18)"; ctx.lineWidth = clampR((active ? 4 : 2.4) * s, 1.2, active ? 3.5 : 2);
    to.forEach(n => road(P, NP[n], 0.06));
  });

  // notables
  const labels = [];
  D.skills.forEach(sk => {
    const p = NP[sk.n], X = sx(p), Y = sy(p), core = CORE.includes(sk.n);
    const r = clampR((core ? 17 : 13) * s * 2.2, core ? 10 : 8, core ? 28 : 24), on = !dim || roleSk.has(sk.n) || core;
    ctx.globalAlpha = on ? 1 : 0.35;
    const shape = () => sk.guard ? poly(X, Y, r * 1.12, 6, Math.PI / 6) : (ctx.beginPath(), ctx.arc(X, Y, r, 0, 6.2832));
    if (isHall(sk)) { ctx.save(); ctx.shadowColor = HALL; ctx.shadowBlur = 22; shape(); ctx.fillStyle = HALL; ctx.fill(); ctx.restore(); }
    if (isEng(sk)) { ctx.save(); ctx.shadowColor = ENG; ctx.shadowBlur = 14; shape(); ctx.fillStyle = ENG; ctx.fill(); ctx.restore(); }
    shape();
    ctx.fillStyle = isHall(sk) ? HALL : isEng(sk) ? ENG : sk.status === "held" ? LIT : "#10232a"; ctx.fill();
    ctx.strokeStyle = isHall(sk) ? "#effffa" : sk.status === "held" ? HALL : LIT; ctx.lineWidth = sk.status === "draft" ? 1.8 : 1.4;
    if (sk.status === "draft") ctx.setLineDash([3, 2.5]);
    ctx.stroke(); ctx.setLineDash([]);
    if (sk.lvl >= 4 && !sk.guard) { ctx.strokeStyle = GOLD; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(X, Y, r + 4, 0, 6.2832); ctx.stroke(); }
    if (sk.cap) { ctx.strokeStyle = ROLE; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.arc(X, Y, r + 4, 0, 6.2832); ctx.stroke(); ctx.beginPath(); ctx.arc(X, Y, r + 7.5, 0, 6.2832); ctx.stroke(); }
    if (core) { ctx.strokeStyle = ROLE; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(X, Y, r + 3, 0, 6.2832); ctx.stroke(); }
    if (sel && sel.k === "skill" && sel.n === sk.n) { ctx.strokeStyle = "#fff"; ctx.lineWidth = 2.2; ctx.beginPath(); ctx.arc(X, Y, r + 10, 0, 6.2832); ctx.stroke(); }
    ctx.globalAlpha = 1;
    if (on) labels.push({ X, Y: Y + r + 7, a: sk.n, b: s >= 0.3 ? sk.t : "", pri: (isHall(sk) ? 3 : 0) + (core ? 2 : 0) + (roleSk.has(sk.n) ? 4 : 0) });
  });
  // keystones
  D.keys.forEach((k, ki) => {
    const p = KP[ki], X = sx(p), Y = sy(p), r = clampR(20 * s * 2.2, 13, 32), all = k.courses.every(c => isHall(SK[c]));
    poly(X, Y, r, 8, Math.PI / 8); ctx.fillStyle = all ? "#6b5a22" : "#231d0c"; ctx.fill();
    ctx.strokeStyle = GOLD; ctx.lineWidth = 2.2; ctx.stroke();
    poly(X, Y, r * 0.62, 8, Math.PI / 8); ctx.lineWidth = 1.2; ctx.stroke();
    if (sel && sel.k === "key" && sel.i === ki) { ctx.strokeStyle = "#fff"; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(X, Y, r + 8, 0, 6.2832); ctx.stroke(); }
    labels.push({ X, Y: Y + r + 8, a: "Keystone", b: k.t, gold: true, pri: 6 });
  });
  // role landmarks
  rolesNow.forEach(([R, P], i) => {
    const X = sx(P), Y = sy(P), r = clampR(34 * s * 1.6, 17, 48), active = role && role.name === R.name;
    const cov = R.need.filter(j => litBy[j]).length / Math.max(1, R.need.length), hall = R.need.filter(j => (litBy[j] || []).some(isHall)).length / Math.max(1, R.need.length);
    ctx.save(); if (active) { ctx.shadowColor = ROLE; ctx.shadowBlur = 24; }
    ctx.beginPath(); ctx.arc(X, Y, r, 0, 6.2832); ctx.fillStyle = "#151d22"; ctx.fill(); ctx.restore();
    ctx.lineWidth = Math.max(3, r * 0.16); ctx.strokeStyle = "rgba(233,228,207,.16)"; ctx.beginPath(); ctx.arc(X, Y, r, 0, 6.2832); ctx.stroke();
    ctx.strokeStyle = LIT; ctx.beginPath(); ctx.arc(X, Y, r, -Math.PI / 2, -Math.PI / 2 + cov * 6.2832); ctx.stroke();
    ctx.strokeStyle = HALL; ctx.beginPath(); ctx.arc(X, Y, r, -Math.PI / 2, -Math.PI / 2 + hall * 6.2832); ctx.stroke();
    ctx.strokeStyle = ROLE; ctx.lineWidth = active ? 2.2 : 1.2; ctx.beginPath(); ctx.arc(X, Y, r + Math.max(3, r * 0.16) / 2 + 3, 0, 6.2832); ctx.stroke();
    ctx.fillStyle = ROLE; ctx.font = `600 ${clampR(r * 0.5, 10, 18)}px "Source Serif 4", Georgia, serif`; ctx.textAlign = "center"; ctx.textBaseline = "middle";
    ctx.fillText(Math.round(cov * 100) + "%", X, Y);
    labels.push({ X, Y: Y + r + 10, a: "Role", b: R.name, role: true, pri: 9 });
  });
  ctx.textAlign = "center"; ctx.textBaseline = "middle";
  const boxes = [];
  const hit = b => boxes.some(q => !(b[2] < q[0] || b[0] > q[2] || b[3] < q[1] || b[1] > q[3]));
  // node labels first (they matter most), then region names where there's room
  labels.sort((x, y) => y.pri - x.pri).forEach(L => {
    const f1 = L.role ? `600 ${s < 0.25 ? 10 : 11}px Inter, sans-serif` : "600 10.5px Inter, sans-serif";
    const f2 = L.role ? `600 ${s < 0.25 ? 14 : 16}px "Source Serif 4", Georgia, serif` : "500 11.5px Inter, sans-serif";
    ctx.font = f2; const bl = L.b ? splitLines(L.b, L.role ? 150 : 130) : [];
    const w = Math.max(40, ...bl.map(l => ctx.measureText(l).width)), h = 13 + bl.length * (L.role ? 17 : 13);
    const box = [L.X - w / 2 - 3, L.Y - 6, L.X + w / 2 + 3, L.Y + h];
    if (hit(box)) return; boxes.push(box);
    ctx.font = f1; ctx.fillStyle = L.gold ? GOLD : L.role ? ROLE + "aa" : "rgba(238,243,241,.95)";
    ctx.fillText(L.role ? "ROLE" : L.a, L.X, L.Y);
    ctx.font = f2; ctx.fillStyle = L.gold ? GOLD : L.role ? ROLE : "rgba(238,243,241,.72)";
    bl.forEach((l, k) => ctx.fillText(l, L.X, L.Y + 13 + k * (L.role ? 17 : 13)));
  });
  if (s < 0.45) {
    ctx.font = "600 13px Inter, sans-serif";
    cats.forEach(c => {
      const gs = order.filter(gi => catOf(gi) === c), cc = mean(gs.map(gi => gwaPos[gi])), d = Math.max(1, Math.hypot(cc.x, cc.y));
      const txt = CATN[c].toUpperCase(), w = ctx.measureText(txt).width;
      for (const R0 of [EXT0 * 0.78, EXT0 * 0.62, EXT0 + 30]) {
        const X = Math.min(W - w / 2 - 8, Math.max(w / 2 + 8, sx({ x: cc.x * R0 / d }))), Y = Math.min(H - 16, Math.max(16, sy({ y: cc.y * R0 / d })));
        const box = [X - w / 2 - 4, Y - 9, X + w / 2 + 4, Y + 9]; if (hit(box)) continue;
        boxes.push(box); ctx.fillStyle = CATC[c] + "cc"; ctx.fillText(txt, X, Y); break;
      }
    });
  }
  if (s >= 0.13) {
    ctx.font = `600 ${s < 0.3 ? 10.5 : 12.5}px Inter, sans-serif`;
    order.slice().sort((x, y) => gwaPos[y].r - gwaPos[x].r).forEach(gi => {
      const b = gwaPos[gi]; if (b.r * s < 18) return;
      const lh = s < 0.3 ? 12 : 14, lines = splitLines(D.gwas[gi][1], Math.max(110, Math.min(200, b.r * s * 1.6))), w = Math.max(...lines.map(l => ctx.measureText(l).width));
      const X = sx(b), Yb = sy(b) - b.r * s - 6, box = [X - w / 2 - 4, Yb - lines.length * lh, X + w / 2 + 4, Yb + 4];
      if (hit(box)) return; boxes.push(box); ctx.fillStyle = "rgba(238,243,241,.5)";
      lines.forEach((l, k) => ctx.fillText(l, X, Yb - (lines.length - 1 - k) * lh - lh / 2));
    });
  }
  if (s >= 0.75) {
    ctx.font = "500 11.5px Inter, sans-serif"; ctx.fillStyle = "rgba(238,243,241,.45)";
    D.iwas.forEach((w, ii) => {
      const c = iwaPos[ii], X = sx(c), Y = sy(c) - c.r * s - 10; if (X < -100 || X > W + 100 || Y < -40 || Y > H + 40) return;
      const lines = splitLines(w[1], 180), bw = Math.max(...lines.map(l => ctx.measureText(l).width)), box = [X - bw / 2 - 3, Y - lines.length * 13, X + bw / 2 + 3, Y + 6];
      if (hit(box)) return; boxes.push(box); wrapText(w[1], X, Y, 180, 13);
    });
  }
  if (s >= 1.8) {
    ctx.font = "11px Inter, sans-serif"; ctx.fillStyle = "rgba(238,243,241,.8)"; ctx.textAlign = "left";
    for (let i = 0; i < D.dwas.length; i++) {
      const X = sx(pos[i]), Y = sy(pos[i]); if (X < 0 || X > W || Y < 0 || Y > H) continue;
      const t = D.dwas[i][0].replace(/\.$/, ""), tw = ctx.measureText(t).width, box = [X + 6, Y - 7, X + 10 + tw, Y + 7];
      if (hit(box)) continue; boxes.push(box); ctx.fillText(t, X + 8, Y);
    }
  }
  drawMini();
  zl.textContent = Math.round(V.s / fitS() * 100) + "%";
}
// ---- the minimap: the whole map, small, with the part in view outlined. Tap or drag it to go there.
const mini = document.getElementById("mini"), mctx = mini.getContext("2d"), zl = document.getElementById("zlvl");
let miniBg = null, MW = 0;
function miniBuild() {
  const r = mini.getBoundingClientRect(); MW = r.width; if (!MW) return null;
  const c = document.createElement("canvas"); c.width = c.height = Math.round(MW * DPR);
  const g = c.getContext("2d"); g.setTransform(DPR, 0, 0, DPR, 0, 0);
  const k = MW / (2 * EXT), mx = p => MW / 2 + p.x * k, my = p => MW / 2 + p.y * k;
  D.gwas.forEach((_, gi) => { const b = gwaPos[gi]; g.beginPath(); g.arc(mx(b), my(b), Math.max(1.5, b.r * k), 0, 6.2832); g.fillStyle = CATC[catOf(gi)] + "22"; g.fill(); });
  for (let i = 0; i < D.dwas.length; i++) { if (!litBy[i]) continue; g.fillStyle = litBy[i].some(isHall) ? HALL : LIT; g.fillRect(mx(pos[i]) - 0.6, my(pos[i]) - 0.6, 1.2, 1.2); }
  D.skills.forEach(sk => { const p = NP[sk.n]; g.beginPath(); g.arc(mx(p), my(p), 1.8, 0, 6.2832); g.fillStyle = isHall(sk) ? HALL : isEng(sk) ? ENG : "#6c8a86"; g.fill(); });
  RP.forEach(p => { g.beginPath(); g.arc(mx(p), my(p), 2.6, 0, 6.2832); g.fillStyle = ROLE; g.fill(); });
  return c;
}
function drawMini() {
  const show = V.s > fitS() * 1.15; mini.hidden = !show; if (!show) return;
  const r = mini.getBoundingClientRect(); if (!r.width) return;
  if (!miniBg || Math.abs(r.width - MW) > 0.5) { mini.width = mini.height = Math.round(r.width * DPR); miniBg = miniBuild(); }
  if (!miniBg) return;
  mctx.setTransform(1, 0, 0, 1, 0, 0); mctx.clearRect(0, 0, mini.width, mini.height); mctx.drawImage(miniBg, 0, 0);
  mctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  const k = MW / (2 * EXT), x0 = MW / 2 + (-V.x / V.s) * k, y0 = MW / 2 + (-V.y / V.s) * k, w = W / V.s * k, h = H / V.s * k;
  mctx.strokeStyle = "#eef3f1"; mctx.lineWidth = 1.4; mctx.strokeRect(Math.max(0.7, x0), Math.max(0.7, y0), Math.min(MW - 1.4, w), Math.min(MW - 1.4, h));
  if (w < 6 && h < 6) { mctx.beginPath(); mctx.arc(x0 + w / 2, y0 + h / 2, 4, 0, 6.2832); mctx.stroke(); }
}
function miniGo(e) { const r = mini.getBoundingClientRect(), k = r.width / (2 * EXT); stopAnim(); const c = { x: (e.clientX - r.left - r.width / 2) / k, y: (e.clientY - r.top - r.height / 2) / k }; V.x = W / 2 - c.x * V.s; V.y = H / 2 - c.y * V.s; draw(); }
mini.addEventListener("pointerdown", e => { e.stopPropagation(); mini.setPointerCapture(e.pointerId); mini.dragging = true; miniGo(e); });
mini.addEventListener("pointermove", e => { if (mini.dragging) miniGo(e); });
mini.addEventListener("pointerup", () => { mini.dragging = false; });
mini.addEventListener("pointercancel", () => { mini.dragging = false; });
function splitLines(t, maxW) { const words = t.split(" "), lines = []; let ln = ""; words.forEach(w => { const tl = ln ? ln + " " + w : w; if (ctx.measureText(tl).width > maxW && ln) { lines.push(ln); ln = w; } else ln = tl; }); if (ln) lines.push(ln); return lines; }
function wrapText(t, x, y, maxW, lh) { const lines = splitLines(t, maxW), y0 = y - (lines.length - 1) * lh; lines.forEach((l, k) => ctx.fillText(l, x, y0 + k * lh)); }

// ---- interaction
let drag = null; const pointers = new Map(); let pinch = null, lastTap = null, anim = null;
function stopAnim() { if (anim) { cancelAnimationFrame(anim); anim = null; } }
// glide to a place and scale: the scale moves evenly on a log scale, so zooming 10x feels as smooth as 2x
function animTo(c1, s1, ms = 300) {
  stopAnim(); const c0 = centerOf(), s0 = V.s, t0 = performance.now();
  const step = now => {
    const k = Math.min(1, (now - t0) / ms), e = 1 - Math.pow(1 - k, 3), ns = Math.exp(Math.log(s0) + (Math.log(s1) - Math.log(s0)) * e);
    const cx = c0.x + (c1.x - c0.x) * e, cy = c0.y + (c1.y - c0.y) * e;
    V.s = ns; V.x = W / 2 - cx * ns; V.y = H / 2 - cy * ns; draw();
    anim = k < 1 ? requestAnimationFrame(step) : null;
  };
  anim = requestAnimationFrame(step);
}
function zoomBy(px, py, f, ms = 260) { const s1 = clampS(V.s * f), wx = (px - V.x) / V.s, wy = (py - V.y) / V.s; animTo({ x: wx - (px - W / 2) / s1, y: wy - (py - H / 2) / s1 }, s1, ms); }
function zoomAt(px, py, f) { stopAnim(); const ns = clampS(V.s * f); f = ns / V.s; V.x = px - (px - V.x) * f; V.y = py - (py - V.y) * f; V.s = ns; draw(); }
function flyTo(p, s1) { animTo({ x: p.x, y: p.y }, clampS(s1 || Math.max(V.s, fitS() * 4)), 420); }
const mid = () => { const [a, b] = [...pointers.values()]; return { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2, d: Math.hypot(a.x - b.x, a.y - b.y) }; };
cv.addEventListener("pointerdown", e => {
  stopAnim(); cv.setPointerCapture(e.pointerId); pointers.set(e.pointerId, { x: e.offsetX, y: e.offsetY });
  if (pointers.size === 1) drag = { x: e.offsetX, y: e.offsetY, vx: V.x, vy: V.y, moved: false };
  else if (pointers.size === 2) { const m = mid(); pinch = { d: Math.max(1, m.d), s: V.s, wx: (m.x - V.x) / V.s, wy: (m.y - V.y) / V.s }; drag = null; }
});
cv.addEventListener("pointermove", e => {
  if (!pointers.has(e.pointerId)) return; pointers.set(e.pointerId, { x: e.offsetX, y: e.offsetY });
  if (pinch && pointers.size === 2) { const m = mid(), ns = clampS(pinch.s * m.d / pinch.d); V.s = ns; V.x = m.x - pinch.wx * ns; V.y = m.y - pinch.wy * ns; draw(); return; }
  if (drag) { const dx = e.offsetX - drag.x, dy = e.offsetY - drag.y; if (Math.abs(dx) + Math.abs(dy) > 4) { drag.moved = true; cv.classList.add("drag"); } V.x = drag.vx + dx; V.y = drag.vy + dy; draw(); }
});
cv.addEventListener("pointerup", e => {
  const d = drag, wasPinch = !!pinch; pointers.delete(e.pointerId); if (pointers.size < 2) pinch = null; cv.classList.remove("drag"); drag = null;
  if (!d || d.moved || wasPinch) return;
  const now = performance.now();
  if (lastTap && now - lastTap.t < 330 && Math.hypot(lastTap.x - e.offsetX, lastTap.y - e.offsetY) < 26) { zoomBy(e.offsetX, e.offsetY, e.shiftKey ? 0.4 : 2.5); lastTap = null; }
  else { pick(e.offsetX, e.offsetY); lastTap = { t: now, x: e.offsetX, y: e.offsetY }; }
});
cv.addEventListener("pointercancel", e => { pointers.delete(e.pointerId); drag = null; pinch = null; cv.classList.remove("drag"); });
// mouse wheels zoom; trackpads pinch (ctrlKey) to zoom and swipe sideways to move
cv.addEventListener("wheel", e => {
  e.preventDefault();
  const u = e.deltaMode === 1 ? 33 : e.deltaMode === 2 ? 400 : 1, dx = e.deltaX * u, dy = e.deltaY * u;
  if (!e.ctrlKey && Math.abs(dx) > Math.abs(dy)) { stopAnim(); V.x -= dx; V.y -= dy; draw(); return; }
  zoomAt(e.offsetX, e.offsetY, Math.exp(-dy * (e.ctrlKey ? 0.012 : 0.0024)));
}, { passive: false });
document.getElementById("zin").onclick = () => zoomBy(W / 2, H / 2, 2);
document.getElementById("zout").onclick = () => zoomBy(W / 2, H / 2, 0.5);
document.getElementById("zfit").onclick = () => animTo({ x: 0, y: 0 }, fitS(), 380);
// ---- full screen: the map fills the screen, with the node card floating on it
const box = document.querySelector(".mapbox"), fsBtn = document.getElementById("zfs"), detailEl = document.getElementById("detail"), detailHome = detailEl.parentNode, detailNext = detailEl.nextSibling;
const ICON_IN = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M3 8V3h5M17 8V3h-5M3 12v5h5M17 12v5h-5"/></svg>';
const ICON_OUT = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M8 3v5H3M12 3v5h5M8 17v-5H3M12 17v-5h5"/></svg>';
const reqFS = box.requestFullscreen || box.webkitRequestFullscreen;
const fsEl = () => document.fullscreenElement || document.webkitFullscreenElement;
const isFull = () => fsEl() === box || box.classList.contains("full");
function setFull(on) {
  if (on) {
    if (reqFS) { try { const p = reqFS.call(box); if (p && p.catch) p.catch(() => { box.classList.add("full"); afterFull(); }); } catch (err) { box.classList.add("full"); afterFull(); } }
    else { box.classList.add("full"); afterFull(); }
  } else {
    if (fsEl()) (document.exitFullscreen || document.webkitExitFullscreen).call(document);
    box.classList.remove("full"); afterFull();
  }
}
function afterFull() {
  const on = isFull();
  document.body.classList.toggle("noscroll", box.classList.contains("full"));
  box.classList.toggle("isfull", on);
  fsBtn.innerHTML = on ? ICON_OUT : ICON_IN; fsBtn.setAttribute("aria-label", on ? "Leave full screen" : "Full screen"); fsBtn.title = on ? "Leave full screen (Esc)" : "Full screen (F)";
  if (on && detailEl.parentNode !== box) { box.appendChild(detailEl); detailEl.classList.add("fsdetail"); box.classList.toggle("nodetail", W < 600 || window.innerWidth < 600); }
  if (!on && detailEl.parentNode === box) { detailHome.insertBefore(detailEl, detailNext); detailEl.classList.remove("fsdetail"); }
  requestAnimationFrame(resize);
}
fsBtn.innerHTML = ICON_IN; fsBtn.onclick = () => setFull(!isFull());
document.getElementById("zinfo").onclick = () => box.classList.toggle("nodetail");
document.addEventListener("fullscreenchange", afterFull); document.addEventListener("webkitfullscreenchange", afterFull);
// keys, when the map has focus or fills the screen: + and - zoom, 0 shows it all, arrows move, F full screen, Esc leaves
cv.tabIndex = 0;
document.addEventListener("keydown", e => {
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  const t = e.target, typing = t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA");
  if (typing || !(box.contains(t) || isFull())) return;
  const k = e.key, step = 90;
  if (k === "+" || k === "=") zoomBy(W / 2, H / 2, 1.6);
  else if (k === "-" || k === "_") zoomBy(W / 2, H / 2, 1 / 1.6);
  else if (k === "0") animTo({ x: 0, y: 0 }, fitS(), 380);
  else if (k === "f" || k === "F") setFull(!isFull());
  else if (k === "Escape" && isFull()) setFull(false);
  else if ((k === "i" || k === "I") && isFull()) box.classList.toggle("nodetail");
  else if (k.startsWith("Arrow")) { stopAnim(); V.x += k === "ArrowLeft" ? step : k === "ArrowRight" ? -step : 0; V.y += k === "ArrowUp" ? step : k === "ArrowDown" ? -step : 0; draw(); }
  else return;
  e.preventDefault();
});
function pick(px, py) {
  box.classList.remove("nodetail");
  const near = (p, r) => Math.hypot(sx(p) - px, sy(p) - py) <= r;
  const rolesNow = RL.map((R, i) => [R, RP[i]]); if (tempRP) rolesNow.push(tempRP);
  for (const [R, P] of rolesNow) if (near(P, clampR(34 * V.s * 1.6, 17, 48) + 4)) { sel = { k: "role", R }; setRoleObj(R); return; }
  for (let ki = 0; ki < D.keys.length; ki++) if (near(KP[ki], clampR(20 * V.s * 2.2, 13, 32) + 4)) { sel = { k: "key", i: ki }; detail(); draw(); return; }
  for (const sk of D.skills) if (near(NP[sk.n], clampR(13 * V.s * 2.2, 7, 28) + 6)) { sel = { k: "skill", n: sk.n }; detail(); draw(); return; }
  let best = null, bd = 16;
  for (let i = 0; i < D.dwas.length; i++) { const d = Math.hypot(sx(pos[i]) - px, sy(pos[i]) - py); if (d < bd) { bd = d; best = i; } }
  if (best === null) return;
  sel = { k: "dwa", i: best }; detail(); draw();
}
// Points (Innovation Board 85.3): 1 point is about 100 tokens of context. One agent carries up to 190 points and 30 skills,
// the load the Context Budget experiment showed safe on every engine tested (about 19,000 tokens, 33 skills).
const BUDGET = 190, MAXSK = 30;
const ptsOf = list => list.reduce((a, sk) => a + (sk && sk.pts || 0), 0);
function budgetLine(list) {
  const p = ptsOf(list), n = list.length, over = p > BUDGET || n > MAXSK;
  return `<p><b>${p} points</b> across ${n} skill${n === 1 ? "" : "s"}, of one agent's ${BUDGET} points and ${MAXSK} skills.${over ? " That's more than one agent can carry: split it across agents." : p > BUDGET * 0.7 ? " Near the top of the budget: on small engines (Haiku, nano), that's where they started to drift." : ""}</p>`;
}
const esc = t => String(t).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
function statusWord(sk) { return isHall(sk) ? "Hallmarked" : isEng(sk) ? engWord(sk) : sk.status === "held" ? "Passed, held for review" : "Built, not yet proven"; }
function chip(sk) { const h = isHall(sk); return `<button type="button" class="chip ${h ? "hall" : sk.status === "held" ? "lit" : ""}" data-sk="${esc(sk.n)}">${esc(sk.n)} ${esc(sk.t)}${h ? " · Hallmarked" : isEng(sk) ? " · Hallmarked, small engines" : sk.status === "held" ? " · held" : ""}</button>`; }
const MODEL = { "claude-haiku-5-5": "Haiku 5.5", "claude-sonnet-5-5": "Sonnet 5.5", "gpt-5.5": "GPT-5.5", "gpt-5.4-nano": "GPT-5.4 nano" };
function detail() {
  const el = document.getElementById("detail");
  if (!sel) {
    el.innerHTML = `<div class="lbl">Tap any node</div><h2>${D.dwas.length.toLocaleString()} requirements, ${D.skills.length} skills so far</h2><p>Small dots are what jobs ask for, from O*NET. Big nodes are skills a builder has written. Gold octagons are keystones, the powers an owner signs for. Roles sit on the rim.</p>`;
  } else if (sel.k === "skill") {
    const sk = SK[sel.n], models = Object.entries(sk.models || {});
    const kind = CORE.includes(sk.n) ? "Core skill" : sk.guard ? "Guard skill" : sk.cap ? "Role skill (capstone)" : sk.lvl >= 4 ? "Keystone skill" : "Skill";
    el.innerHTML = `<div class="lbl">${kind} · ${statusWord(sk)}</div><h2>${esc(sk.n)} ${esc(sk.t)}</h2>
      <p>Lets an agent: ${esc(DOES[sk.does] || sk.does)} (level ${sk.lvl}00).${sk.guard ? " A Guard skill: the safety habits that must come before the risky ones." : ""}${keyOf[sk.n] ? ` Part of the ${keyOf[sk.n].map(k => esc(k.t)).join(", ")} keystone.` : ""}</p>
      ${sk.pts ? `<p>Costs <b>${sk.pts} point${sk.pts === 1 ? "" : "s"}</b> of an agent's ${BUDGET}: about ${(sk.pts * 100).toLocaleString()} tokens of context when it's used.</p>` : ""}
      ${models.length ? `<div class="chips">${models.map(([m, ok]) => `<span class="chip ${ok ? "hall" : ""}">${MODEL[m] || m} ${ok ? "passed" : "not passed"}</span>`).join("")}</div>` : ""}
      <div class="lbl">Covers</div><div class="chips">${sk.dwas.map(i => `<span class="chip">${esc(D.dwas[i][0].replace(/\.$/, ""))}</span>`).join("")}</div>
      ${sk.pre.length ? `<div class="lbl">Path from</div><div class="chips">${sk.pre.map(n => chip(SK[n])).join("")}</div>` : ""}`;
  } else if (sel.k === "key") {
    const k = D.keys[sel.i];
    el.innerHTML = `<div class="lbl">Keystone</div><h2>${esc(k.t)}</h2><p>${esc(k.summary)}</p>${budgetLine(k.courses.map(n => SK[n]).filter(Boolean))}<div class="lbl">Takes</div><div class="chips">${k.courses.map(n => chip(SK[n])).join("")}</div>`;
  } else if (sel.k === "role") {
    const R = sel.R, cov = R.need.filter(i => litBy[i]).length, hall = R.need.filter(i => (litBy[i] || []).some(isHall)).length;
    const sks = [...roleSk].map(n => SK[n]).filter(Boolean).sort((a, b) => a.n.localeCompare(b.n));
    el.innerHTML = `<div class="lbl">Role${R.build ? " · " + esc(R.build) + " build" : ""}</div><h2>${esc(R.name)}</h2>
      <p>${R.occ != null ? `Measured against O*NET's ${esc(D.occs[R.occ][1])} (${D.occs[R.occ][0]}): ` : "Measured against its build's skills: "}<b>${cov} of ${R.need.length}</b> requirements covered, ${hall} Hallmarked.${R.cap ? ` Its capstone is ${esc(R.cap)}.` : R.occ != null && !R.cap && R.courses.length ? " No capstone yet: this role is still being built." : ""}</p>
      ${sks.length ? budgetLine(sks) : ""}
      <div class="lbl">Skills on this path</div><div class="chips">${sks.map(chip).join("") || '<span class="chip">None yet</span>'}</div>`;
  } else {
    const d = D.dwas[sel.i], iw = D.iwas[d[1]], gw = D.gwas[iw[2]], lit = litBy[sel.i] || [];
    el.innerHTML = `<div class="lbl">Requirement</div><h2>${esc(d[0])}</h2>
      <div class="path">${CATN[gw[0].slice(0, 5)]} › ${esc(gw[1])} › ${esc(iw[1])}</div>
      <p>${needCount[sel.i].toLocaleString()} of ${D.occs.length} jobs ask for this.${roleSet.has(sel.i) ? " It's on the chosen role's path." : ""}</p>
      <div class="chips">${lit.length ? lit.map(chip).join("") : '<span class="chip">Dark: no skill yet. Open for a builder.</span>'}</div>`;
  }
  el.querySelectorAll("[data-sk]").forEach(b => b.onclick = () => { sel = { k: "skill", n: b.dataset.sk }; detail(); if (NP[b.dataset.sk]) flyTo(NP[b.dataset.sk]); else draw(); });
}

// ---- roles
const q = document.getElementById("q"), res = document.getElementById("results");
q.addEventListener("input", () => {
  const v = q.value.trim().toLowerCase();
  if (v.length < 2) { res.hidden = true; return; }
  const words = v.split(/\s+/);
  const named = RL.filter(R => words.every(w => R.name.toLowerCase().includes(w))).map(R => `<button type="button" data-r="${RL.indexOf(R)}">${esc(R.name)}<small>role</small></button>`);
  const hits = D.occs.map((o, i) => [o, i]).filter(([o]) => words.every(w => o[1].toLowerCase().includes(w))).slice(0, 12);
  res.innerHTML = named.concat(hits.map(([o, i]) => `<button type="button" data-i="${i}">${esc(o[1])}<small>${o[0]}</small></button>`)).join("") || `<button type="button" disabled>No job matches “${esc(v)}”</button>`;
  res.hidden = false;
  res.querySelectorAll("button[data-i]").forEach(b => b.onclick = () => { setOcc(+b.dataset.i); res.hidden = true; });
  res.querySelectorAll("button[data-r]").forEach(b => b.onclick = () => { const R = RL[+b.dataset.r]; sel = { k: "role", R }; setRoleObj(R); res.hidden = true; });
});
q.addEventListener("keydown", e => { if (e.key === "Escape") res.hidden = true; });
document.addEventListener("click", e => { if (!e.target.closest(".search")) res.hidden = true; });
document.getElementById("clearRole").onclick = () => { role = null; roleSet = new Set(); roleSk = new Set(); tempRP = null; sel = null; q.value = ""; roleStat(); detail(); draw(); };
function setOcc(i) {
  const lm = RL.find(R => R.occ === i);
  if (lm) { sel = { k: "role", R: lm }; setRoleObj(lm); return; }
  const R = { name: D.occs[i][1], build: null, cap: null, occ: i, need: D.occs[i][2], courses: [] };
  const a = roleAnchor(R); tempRP = [R, { x: (RIM + 40) * Math.cos(a), y: (RIM + 40) * Math.sin(a) }];
  sel = { k: "role", R }; setRoleObj(R);
}
function setRoleObj(R) {
  if (!(tempRP && tempRP[0] === R)) tempRP = null;
  role = R; roleSet = new Set(R.need); roleSk = roleSkills(R); q.value = R.name; roleStat(); detail(); draw();
  try { localStorage.setItem("map-role2", R.occ != null ? D.occs[R.occ][0] : "role:" + R.name); } catch (e) {}
}
function roleStat() {
  const el = document.getElementById("rolestat");
  if (!role) { el.innerHTML = "No role chosen. Tap a role on the rim, or search any job."; return; }
  const need = role.need, cov = need.filter(i => litBy[i]).length, hall = need.filter(i => (litBy[i] || []).some(isHall)).length;
  el.innerHTML = `<b>${cov} of ${need.length}</b> requirements covered <span class="cov"><i style="width:${100 * cov / need.length}%"></i></span> · ${hall} Hallmarked`;
}
const nHall = Object.keys(litBy).filter(i => litBy[i].some(isHall)).length;
document.getElementById("stats").innerHTML = [
  [D.dwas.length.toLocaleString(), "requirements"], [D.skills.length, "skills"], [D.skills.filter(isHall).length, "Hallmarked"], [D.skills.filter(isEng).length, "for small engines"],
  [D.keys.length, "keystones"], [RL.length, "roles"]].map(([b, t]) => `<div class="stat"><b>${b}</b><span>${t}</span></div>`).join("");

// start on the Enterprise AE role, unless the viewer chose another before
window.addEventListener("resize", resize);
if (window.ResizeObserver) new ResizeObserver(() => resize()).observe(box);
resize();
let startR = RL.find(R => R.name === "Enterprise Account Executive");
try {
  const saved = localStorage.getItem("map-role2");
  if (saved && saved.startsWith("role:")) startR = RL.find(R => R.name === saved.slice(5)) || startR;
  else if (saved && occByCode[saved] != null) { setOcc(occByCode[saved]); startR = null; }
} catch (e) {}
if (startR) { sel = { k: "role", R: startR }; setRoleObj(startR); }
detail();
