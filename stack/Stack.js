class Stack {

    constructor () {
        this.length = 0;
        this.head = undefined;
    }

    push (item) {
        const node = { value: item };
        this.length ++;

        if (!this.head) {
            this.head = node;
            return;
        }

        node.prev = this.head;
        this.head = node;
    }

    pop () {
        this.length = Math.max(0, this.length - 1);
        
        if ( this.length === 0 ) {
            // Delete the remaining head
            const head = this.head;
            this.head = undefined;
            return head?.value;
        }

        const head = this.head;
        this.head = head?.prev;
        return head?.value;
    }

    peek () {
        return this.head?.value;
    }

    fromArray (array) {
        if (!array) return; // Avoid undefined scenario
        if (array?.length === 0) return; // Avoid empty array scenario

        let lo = 0;
        let hi = array.length;
        while (lo < hi) {
            const node = { value: array[lo] };
            this.length++;
            if (!this.head) {
                this.head = node;
            } else {
                node.prev = this.head;
                this.head = node;
            }
            lo++;
        } 
    }

}

module.exports = { Stack }