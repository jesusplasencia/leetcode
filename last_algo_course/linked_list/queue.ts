type Node<T> = {
    value: T,
    next?: Node<T>,
}

export default class Queue<T> {
    public length: number;
    private head?: Node<T>;
    private tail?: Node<T>;

    constructor() {
        this.head = this.tail = undefined;
        this.length = 0;
    }

    enqueue(item: T): void {
        const node = { value: item } as Node<T>;
        
        if (this.length === 0) { // If no nodes, set head and tail to node
            this.head = this.tail = node;
        } else if (this.tail) { // If tail exists, append node to tail
            this.tail.next = node;
            this.tail = node;
        }

        this.length++;
    }
    
    deque(): T | undefined {
        if (!this.head) return undefined;

        this.length--;
        const head = this.head;     // Save reference to head
        this.head = this.head.next; // Move head to next node
        head.next = undefined;      // Free up memory

        return head?.value;    // Return value of old head
    }

    peek(): T | undefined {
        return this.head?.value;
    }
}