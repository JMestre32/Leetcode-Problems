class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_pixel = image[sr][sc]

        self.dfs(image, sr, sc, color, starting_pixel)

        return image

    def dfs(self, image, sr, sc, color, starting_pixel):
        
        if sr < 0 or sr > len(image)-1 or sc < 0 or sc > len(image[0])-1 or image[sr][sc] == color or image[sr][sc] != starting_pixel:
            return
        image[sr][sc] = color
        self.dfs(image, sr+1, sc, color, starting_pixel)
        self.dfs(image, sr-1, sc, color, starting_pixel)
        self.dfs(image, sr, sc+1, color, starting_pixel)
        self.dfs(image, sr, sc-1, color, starting_pixel)


# Topics:
# Matrix
# Arrays
# DFS

# Conceptual Answer:
# So, we're given the color and the starting row/column. What we want to do is initialize the starting_pixel, this is crucial. Otherwise, we won't have something to compare each
# cell to. Next, we recursively call dfs to change adjacent pixels to the desired color IF and only if we are within bounds, the cell's color isn't already the desired color, AND
# the cell has the same pixel value as starting pixel. 
# We find the rows by using len(image) which just tells us how many lists are in image. We find columns by finding len(image[0]) which tells us how many elements are in each row,
# effectively this gives us how many columns we have. 