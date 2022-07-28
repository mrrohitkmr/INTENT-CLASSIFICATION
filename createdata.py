with open("/home/bot/testrasanlu/cities.txt") as f:
    with open("/home/bot/testrasanlu/cities.jsonl","w") as t:
        for line in f:
            line=line.strip(" ")
            lines=line.split(" ")
            count=0
            count1=0
            text=""
            for i in lines:
                if count==0 and len(lines)!=count+1 :
                    text='''{"label":"LOC","pattern":[{"LOWER":"'''+f'{i}"'
                elif count==0:
                    i=i.replace("\n","")
                    text='''{"label":"LOC","pattern":[{"LOWER":"'''+f'{i}"'+"}]}\n"
                elif len(lines)==count+1:
                    i=i.replace("\n","")
                    text+='''},{"LOWER":"'''+f"{i}"+'''"}]}\n'''
                else:
                    text+='''},{"LOWER":"'''+f'{i}"'
                count+=1
            count1+=1   

            t.write(text)
