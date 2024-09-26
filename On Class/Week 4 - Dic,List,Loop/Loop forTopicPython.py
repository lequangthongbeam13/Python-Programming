Course = {
    'Python basics':{
        'content':[
            'condition','loop','function','data type'
            ],
        'credits': 4
    },
    'Database':{
        'content':[    
            'Setup', 'CRUD', 'Relation','Joins'
            ],
        'credits':5
    }
}

# for i in Course:
#     print(f"Content of {i}")
#     for k in Course[i]['content']:
#         print (k)

for course ,detail in Course.items():
    print(f"Content of {Course}")
    for content in detail['content']:
        print (content)

