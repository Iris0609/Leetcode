
##48ms,84.55%
##medium
##bfs

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic={}
        indegree=[0]*numCourses
        
        for l in prerequisites:
            course=l[0]
            pre=l[1]
            if pre not in dic:
                dic[pre]=[course]
            else:
                dic[pre].append(course)
            
            indegree[course]+=1
            
        dq=deque()
        cnt=0
        for i in range(numCourses):
            if indegree[i]==0:
                dq.append(i)
                
        while dq:
            pre=dq.popleft()
            cnt+=1
            if pre in dic:
                course=dic[pre]   
                for c in course:
                    indegree[c]-=1
                    if indegree[c]==0:
                        dq.append(c)
        #print(dq,cnt)
        if sum(indegree)==0:
            return True
        else:
            return False
            
            
        
                
                

            