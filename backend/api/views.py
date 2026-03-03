from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Conversation
from .serializers import QuestionSerializer
from .services.graph import build_graph


graph = build_graph()


class AskQuestionAPIView(APIView):

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        question = serializer.validated_data["question"]

        # Run LangGraph
        result = graph.invoke({"question": question})

        plan = result.get("plan")
        answer = result.get("answer")

        # Save in PostgreSQL
        Conversation.objects.create(
            question=question,
            plan=plan,
            answer=answer
        )

        return Response({
            "question": question,
            "plan": plan,
            "answer": answer
        })