import adjectives from "adjectives";

export function getRandomAdjective() {
    return adjectives[Math.floor(Math.random() * adjectives.length)];
}