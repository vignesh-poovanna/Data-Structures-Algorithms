class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for sublist in image:
            sublist.reverse()
            for i in range(len(sublist)):
                if sublist[i]==1:
                    sublist[i]=0
                else:
                    sublist[i]=1
        
        return image
        
        

        