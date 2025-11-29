from ..extensions import db
from ..models.workflow import Workflow, WorkflowStep
from ..tasks.ai_tasks import analyze_proposal_task
import uuid

def start_workflow(data, user_id):
    workflow = Workflow(
        name=data['name'],
        user_id=user_id,
        status='started'
    )
    db.session.add(workflow)
    db.session.commit()
    
    # Cria step inicial
    step = WorkflowStep(
        workflow_id=workflow.id,
        step_name='init',
        status='running'
    )
    db.session.add(step)
    db.session.commit()
    
    # Se for proposal, dispara IA
    if data['name'] == 'proposal_approval':
        analyze_proposal_task.delay(workflow.id, data['payload']['text'])
    
    return workflow.id