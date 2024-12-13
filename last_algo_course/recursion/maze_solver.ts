const dir = [
    [-1, 0], // Left
    [1, 0],  // Right
    [0, -1], // Up
    [0, 1]   // Down
]

function walk (maze: string[], wall: string, curr: Point, end: Point, seen: boolean[][], path: Point[]): boolean {
    // 1. Off the map
    if (curr.x < 0 || curr.x >= maze[0].length || curr.y < 0 || curr.y >= maze.length) return false;
    // 2. Hit a Wall
    if (maze[curr.y][curr.x] === wall) return false;
    // 3. Reached End
    if (curr.x === end.x && curr.y === end.y) {
        path.push(curr);
        return true;
    }
    // 4. Point have been there
    if (seen[curr.y][curr.x]) return false;

    // Pre-condition
    seen[curr.y][curr.x] = true;
    path.push(curr);

    // Recurse
    for (let i = 0; i < dir.length; ++i) {
        const [x, y] = dir[i];
        const newCurr = {
            x: curr.x + x,
            y: curr.y + y
        };
        if (walk(maze, wall, newCurr, end, seen, path)) return true;
    }

    // Post-operation
    path.pop();
    return false;
}

export default function solve(maze: string[], wall: string, start: Point, end: Point): Point[] {
    const seen: boolean[][] = [];
    const path: Point[] = [];

    for (let i = 0; i < maze.length; ++i) {
        seen.push(new Array(maze[0].length).fill(false)); // Initialize the seen array
    }

    walk(maze, wall, start, end, seen, path);
    return path;
}