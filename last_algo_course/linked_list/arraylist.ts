export default class ArrayList<T> {
    public length: number;
    private data: T[];
    private capacity: number;
    
    constructor() {
        this.length = 0;
        this.capacity = 3;
        this.data = new Array(this.capacity); // Initialize the array with a capacity of 3
    }

    prepend(item: T): void {
        if (this.length === this.capacity) {
            this.growCapacity();
        } else {
            // Shift all the elements to the right by one
            for (let i = this.length - 1; i >= 0; i--) {
                this.data[i + 1] = this.data[i];
            }
        }
        this.data[0] = item; // Add the item to the beginning of the array
        this.length++; // Increment the length
    }
    
    insertAt(item: T, idx: number): void {
        if (this.length === this.capacity) {
            this.growCapacity();
        }
        // Shift all the elements to the right by one starting from idx
        for (let i = this.length - 1; i >= idx; i--) {
            this.data[i + 1] = this.data[i];
        }
        // Add the item to the array at idx
        this.data[idx] = item;
        // Increment the length
        this.length++;
    }

    append(item: T): void {
        if (this.length === this.capacity) {
            this.growCapacity();
        }
        // Add the item to the end of the array
        this.data[this.length] = item;
        // Increment the length
        this.length++;
    }
    
    remove(item: T): T | undefined {
        if (this.length === 0) return undefined;
        for (let i = 0; i < this.length; i++) {
            if (this.data[i] === item) {
                // Shift all the elements to the left by one
                for (let j = i; j < this.length - 1; j++) {
                    this.data[j] = this.data[j + 1];
                }
                // Decrement the length
                this.length--;
                return item;
            }
        }
        return undefined;
    }
    
    get(idx: number): T | undefined {
        if (idx < 0 || idx >= this.length) return undefined;
        return this.data[idx];
    }

    removeAt(idx: number): T | undefined {
        if (this.length === 0) return undefined;
        for (let i = 0; i < this.length; i++) {
            if (i === idx) {
                const item = this.data[i];
                // Shift all the elements to the left by one
                for (let j = i; j < this.length - 1; j++) {
                    this.data[j] = this.data[j + 1];
                }
                // Decrement the length
                this.length--;
                return item;
            }
        }
        return undefined;
    }

    toArray(): T[] | undefined {
        return this?.data;
    }

    private growCapacity(): void {
        // Log Message Growing
        console.log(`Growing from ${this.capacity} to ${this.capacity * 2}`); 
        // Create a new array with double the capacity
        const newData = new Array(this.capacity * 2);
        // Copy the data from the old array to the new array
        for (let i = 0; i < this.length; i++) {
            newData[i] = this.data[i];
        }
        // Update the data reference to point to the new array
        this.data = newData;
        // Update the capacity
        this.capacity *= 2;
    }
}