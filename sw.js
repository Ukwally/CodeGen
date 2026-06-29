const { cache } = require("react");

const CACHE_NAME = 'versao-1';
const ASSETS = [
    '/',
    '/index.html',
    '/manifest.json'
];

//instala o service worker e guarda os arquivos principais no cache
self.addEventListener('install',
    (e) => {
        e.waitUntil(
            cache.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
        )
    })
//serve os ar   quivos do cache quando o usuario esta offline

self.addEventListener('fetch', (e) => {
    e.respondWith(
        caches.match(e.request).then((response) => response || fetch(e.request))
    );

});