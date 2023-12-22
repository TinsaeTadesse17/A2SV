class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(image)):
            image[i].reverse()
        
        for i in range(len(image)):
            for j in range(len(image)):
                if image[i][j]:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        
        return image
