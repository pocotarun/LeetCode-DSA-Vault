type Fn = (...params: any[]) => any

function memoize(fn: Fn): Fn {
    const cache: Record<string, any> = {};

    return function (...args: any[]) {
        const key = JSON.stringify(args);
        if (key in cache) {
            return cache[key];
        }
        const result = fn(...args);
        cache[key] = result;
        return result;
    }
}