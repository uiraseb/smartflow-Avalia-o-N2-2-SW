from celery import shared_task
from ..services.ai_service import analyze_text
from ..extensions import db
from ..models.workflow import WorkflowStep
from ..services.notifications import send_slack_notification

@shared_task
def analyze_proposal_task(workflow_id, text):
    result = analyze_text(text)
    step = WorkflowStep(
        workflow_id=workflow_id,
        step_name='ai_analysis',
        result=result,
        status='completed'
    )
    db.session.add(step)
    db.session.commit()
    
    send_slack_notification(f"Análise IA para workflow {workflow_id}: {result[:50]}...")
    return result