class SnapshotArray:

    def __init__(self, length: int):
        """
        Initializes a new SnapArray object with a specified length.

        Args:
        - length (int): The length of the array to be created.

        Attributes:
        - snap_id (int): The current snapshot ID.
        - data (dict): The dictionary that stores the elements of the array.
        """
        self.snap_id = 0
        self.data = {i: {0: 0} for i in range(length)}

    def set(self, index: int, val: int) -> None:
        """
        Updates the value at a given index in the current snapshot.

        Args:
            index (int): The index to be updated.
            val (int): The new value.
        """
        self.data[index][self.snap_id] = val

    def snap(self) -> int:
        """
        Take a snapshot of the snapshot array and return the snapshot id.
        Returns:
            int: The id of the current snapshot.
        """
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        """
        Returns the value at the given index and snap_id.
        
        Parameters:
            index (int): The index of the data to retrieve.
            snap_id (int): The snap_id of the data to retrieve.
        
        Returns:
            int: The value at the given index and snap_id.
        """
        if snap_id not in self.data[index]:
            max_snap_id = max(id for id in self.data[index] if id <= snap_id)
            return self.data[index][max_snap_id]
        return self.data[index][snap_id]

