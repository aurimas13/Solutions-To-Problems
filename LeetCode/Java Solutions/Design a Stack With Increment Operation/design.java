class CustomStack {
    private int[] stack;
    private int[] increment;
    private int top;
    private int maxSize;

    public CustomStack(int maxSize) {
        this.stack = new int[maxSize];
        this.increment = new int[maxSize];
        this.top = -1;
        this.maxSize = maxSize;
    }
    
    public void push(int x) {
        if (top < maxSize - 1) {
            top++;
            stack[top] = x;
        }
    }
    
    public int pop() {
        if (top == -1) {
            return -1;
        }
        int result = stack[top] + increment[top];
        if (top > 0) {
            increment[top - 1] += increment[top];
        }
        increment[top] = 0;
        top--;
        return result;
    }
    
    public void increment(int k, int val) {
        int i = Math.min(k - 1, top);
        if (i >= 0) {
            increment[i] += val;
        }
    }
}