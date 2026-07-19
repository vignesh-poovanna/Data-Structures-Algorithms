class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for sublist in image:
            sublist.reverse()
            for i in range(len(sublist)):
                sublist[i]= sublist[i]^ 1
        
        return image
        
        

        