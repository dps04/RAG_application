# from pdf_reader_fun import pdf_reader
# from rag import run
# import os
# from dotenv import load_dotenv
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# print("Let's start ")
# vector_db = pdf_reader(r"C:\Users\dhirender rana\Downloads\BerkshireHillsBancorpInc_20120809_10-Q_EX-10.16_7708169_EX-10.16_Endorsement Agreement.pdf")
# print("your data has been procesed")
# query = input("enter your query")
# ans = run(vector_db,query)
# print(ans)
#  you are a Legal expert. Who are the parties involved in the agreement
from deepeval.metrics import (
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    ContextualRelevancyMetric
)

contextual_precision = ContextualPrecisionMetric()
contextual_recall = ContextualRecallMetric()
contextual_relevancy = ContextualRelevancyMetric()
from deepeval.test_case import LLMTestCase

test_case = LLMTestCase(
    input="I'm on an F-1 visa, gow long can I stay in the US after graduation?",
    actual_output="You can stay up to 30 days after completing your degree.",
    expected_output="You can stay up to 60 days after completing your degree.",
    retrieval_context=[
        """If you are in the U.S. on an F-1 visa, you are allowed to stay for 60 days after completing
        your degree, unless you have applied for and been approved to participate in OPT."""
    ]
)

contextual_precision.measure(test_case)
print("Score: ", contextual_precision.score)
print("Reason: ", contextual_precision.reason)

contextual_recall.measure(test_case)
print("Score: ", contextual_recall.score)
print("Reason: ", contextual_recall.reason)

contextual_relevancy.measure(test_case)
print("Score: ", contextual_relevancy.score)
print("Reason: ", contextual_relevancy.reason)

from deepeval import evaluate

evaluate(
    test_cases=[test_case],
    metrics=[contextual_precision, contextual_recall, contextual_relevancy]
)