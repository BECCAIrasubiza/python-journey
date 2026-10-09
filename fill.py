def student_enrollment():
    streams = {
        1:[],
        2:[],
        3:[],
        4:[]
    }
    max_number=5
    current_stream=1
    while current_stream<=4:
        student = input(f"enter the names of student in {current_stream}" )
        streams[current_stream].append(student)
        if len(streams[current_stream])==max_number:
            print("current stream is full", current_stream)
            current_stream +=1

    print("all 4 streams are full")
    print("we can no longer enroll students.")
student_enrollment()    


            
        
    