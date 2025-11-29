# app/tasks/ai_tasks.py
from celery import shared_task
import openai
import os

@shared_task
def analyze_proposal_task(workflow_id, text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Analise sentimento e risco jurídico desta proposta:\n\n{text}"}],
            temperature=0.3
        )
        result = response.choices[0].message.content

        from ..models import WorkflowStep
        from ..extensions import db
        step = WorkflowStep(workflow_id=workflow_id, step_name="ai_analysis", result=result, status="completed")
        db.session.add(step)
        db.session.commit()

        print(f"\nIA analisou workflow {workflow_id}:\n{result}\n")
    except Exception as e:
        print("Erro na IA:", e)