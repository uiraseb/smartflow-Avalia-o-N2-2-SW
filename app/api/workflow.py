# app/api/workflow.py
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services.workflow_engine import start_workflow
from ..tasks.ai_tasks import analyze_proposal_task

api = Namespace('workflows', description='Workflow operations')

workflow_model = api.model('Workflow', {
    'name': fields.String(required=True),
    'trigger': fields.String(required=True),
    'payload': fields.Raw(required=True)
})

@api.route('/')
class WorkflowList(Resource):
    @jwt_required()
    @api.expect(workflow_model)
    @limiter.limit("10/minute")
    def post(self):
        data = api.payload
        user_id = get_jwt_identity()
        workflow_id = start_workflow(data, user_id)

        # Exemplo: dispara análise de IA assíncrona
        if data['name'] == 'proposal_approval':
            analyze_proposal_task.delay(workflow_id, data['payload']['text'])

        return {"workflow_id": workflow_id, "status": "started"}, 202