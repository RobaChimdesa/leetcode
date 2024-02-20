class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # allPeople = {}
        # originalNames = {}
        # for i in range(len(names)):
        #     if names[i] in allPeople:
        #         # add '1' to the end of the name to signify that its still a new person -> ppl can have same names 
        #         allPeople[names[i] + str(i)] = heights[i]
        #         originalNames[names[i] + str(i)] = names[i]
        #     else:
        #         allPeople[names[i]] = heights[i]
        #         originalNames[names[i]] = names[i]

        # sortedVals = dict(sorted(allPeople.items(), key = lambda item: item[-1], reverse=True))
        # #return sortedVals
        # final = []
        # for names in sortedVals:
        #     final.append(originalNames[names])
        # return final
        people={}
        ordered=[]
        for i in range (len(names)):

            people[heights[i]]=names[i]
        sortedpeople=dict(sorted(people.items(),key=lambda item:item[0], reverse=True))
        for name in sortedpeople:

            ordered.append(people[name])
        return ordered
        