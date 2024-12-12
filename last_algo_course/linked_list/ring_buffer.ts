class RingBuffer<T> {
    private buffer: (T | null)[];
    private capacity: number;
    private head: number;
    private tail: number;
    private size: number;

    constructor(capacity: number) {
        this.capacity = capacity;
        this.buffer = new Array<T | null>(capacity).fill(null);
        this.head = 0;
        this.tail = 0;
        this.size = 0;
    }

    isFull(): boolean {
        return this.size === this.capacity;
    }

    isEmpty(): boolean {
        return this.size === 0;
    }

    enqueue(item: T): void {
        if (this.isFull()) {
            throw new Error("Ring buffer is full");
        }
        this.buffer[this.tail] = item;
        this.tail = (this.tail + 1) % this.capacity;
        this.size++;
    }

    dequeue(): T | null {
        if (this.isEmpty()) {
            throw new Error("Ring buffer is empty");
        }
        const item = this.buffer[this.head];
        this.buffer[this.head] = null;
        this.head = (this.head + 1) % this.capacity;
        this.size--;
        return item;
    }

    peek(): T | null {
        if (this.isEmpty()) {
            return null;
        }
        return this.buffer[this.head];
    }

    getSize(): number {
        return this.size;
    }
}

export default RingBuffer;