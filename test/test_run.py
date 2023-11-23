from emm.query.query import Query

question = "What is the best way to install python packages?"

res = Query().get_res(question)
print(res)
