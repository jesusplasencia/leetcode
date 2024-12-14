class ListNodeCustom<T> {
    val: T;
    next: ListNodeCustom<T> | null;

    constructor(val: T, next: ListNodeCustom<T> | null) {
        this.val = val;
        this.next = next;
    }

    fromArray(arr: T[]): ListNodeCustom<T> | null {
        if (arr.length === 0) return null;
        let head = new ListNodeCustom(arr[0], null);
        let cur = head;
        for (let i = 1; i < arr.length; i++) {
            cur.next = new ListNodeCustom(arr[i], null);
            cur = cur.next;
        }
        return head;
    }

    reverse(): ListNodeCustom<T> | null {
        let cur : ListNodeCustom<T> | null = this;
        let reverseTmp: ListNodeCustom<T> | null = null;
        while (cur) {
            const temp = cur.next;
            cur.next = reverseTmp;
            reverseTmp = cur;
            cur = temp;
        }
        return reverseTmp;
    }

    toArray(): T[] {
        let cur: ListNodeCustom<T> | null = this;
        let res: T[] = [];
        while (cur) {
            res.push(cur.val);
            cur = cur.next;
        }
        return res;
    }

    toString(): string {
        return this.toArray().join(' -> ');
    }

    static fromArray<T>(arr: T[]): ListNodeCustom<T> | null {
        if (arr.length === 0) return null;
        let head = new ListNodeCustom(arr[0], null);
        let cur = head;
        for (let i = 1; i < arr.length; i++) {
            cur.next = new ListNodeCustom(arr[i], null);
            cur = cur.next;
        }
        return head;
    }

    static reverse<T>(head: ListNodeCustom<T> | null): ListNodeCustom<T> | null {
        let cur : ListNodeCustom<T> | null = head;
        let reverseTmp: ListNodeCustom<T> | null = null;
        while (cur) {
            const temp = cur.next;
            cur.next = reverseTmp;
            reverseTmp = cur;
            cur = temp;
        }
        return reverseTmp;
    }

    static toArray<T>(head: ListNodeCustom<T> | null): T[] {
        let cur: ListNodeCustom<T> | null = head;
        let res: T[] = [];
        while (cur) {
            res.push(cur.val);
            cur = cur.next;
        }
        return res;
    }

    static toString<T>(head: ListNodeCustom<T> | null): string {
        return this.toArray(head).join(' -> ');
    }

    isPalindrome(): boolean {
        let slow : ListNodeCustom<T> | null = this;
        if (this === null) return true;
        let fast = this.next;

        while (fast && fast.next) {
            slow = slow?.next ?? null;
            fast = fast.next?.next;
        }

        let second = slow?.next ?? null;
        if (!!slow) slow.next = null;
        let reverseTmp : ListNodeCustom<T> | null = null;

        while (second) {
            const temp = second.next;
            second.next = reverseTmp;
            reverseTmp = second;
            second = temp;
        }

        second = reverseTmp;
        let cur : ListNodeCustom<T> | null = this;

        while (second) {
            const temp1 = cur?.val;
            const temp2 = second?.val;
            if (temp1 !== temp2) return false;

            cur = cur?.next ?? null;
            second = second?.next ?? null;
        }

        return true;
    }
}