class DynamicArray {
private:
    int *arr;
    int capacity;
    int size;
public:
    DynamicArray(int capacity) {
        this->capacity = capacity;
        size = 0;
        arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (size == capacity) {
            resize();
        }
        arr[size] = n;
        size += 1;
    }

    int popback() {
        size--;
        return arr[size];
    }

    void resize() {
        int *arr2 = new int[capacity*2];
        for (int i = 0; i < size; i++) {
            arr2[i] = arr[i];
        }
        delete[] arr;
        arr = arr2;
        capacity *= 2;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};
