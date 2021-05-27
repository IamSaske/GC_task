def dynamic(query):
    print('You can add where clause or order by clause\n for event_date and country')
    print('You can add where clause(by selecting 1)\norder by clause(by selecting 2)\nboth as your choice\nto get better results(by selecting 3)')
    a=int(input())
    if a==1:
         return query+"\n"+input('Add where clause')
    elif(a==2):
            return query+"\n"+input('Add where clause')
    elif(a==3):
            return query+'\n'+input('Add where')


query=input('Enter your query')
a=print(dynamic(query))
