from flask import Blueprint,request,jsonify 
from app import SEOSearchEngineModel

seosearch_bp = Blueprint("seosearch_bp",(__name__))

@seosearch_bp.route('/seo-engine', methods=['POST'])
def create_seo_engine():
    data = request.json
    obj = SEOSearchEngineModel(
        search_engine_name=data['search_engine_name'],
        search_engine_url=data['search_engine_url']
    )
    db.session.add(obj)
    db.session.commit()
    return jsonify({"message": "Created"})

@seosearch_bp.route('/seo-engine', methods=['GET'])
def get_seo_engines():
    data = SEOSearchEngineModel.query.filter_by(is_deleted=False).all()
    return jsonify([{
        "id": i.id,
        "name": i.search_engine_name,
        "url": i.search_engine_url
    } for i in data])

@seosearch_bp.route('/seo-engine/<int:id>', methods=['GET'])
def get_seo_engine(id):
    obj = SEOSearchEngineModel.query.filter_by(id=id, is_deleted=False).first()
    return jsonify({
        "id": obj.id,
        "name": obj.search_engine_name,
        "url": obj.search_engine_url
    })

@seosearch_bp.route('/seo-engine/<int:id>', methods=['PUT'])
def update_seo_engine(id):
    data = request.json
    obj = SEOSearchEngineModel.query.get(id)

    obj.search_engine_name = data.get('search_engine_name', obj.search_engine_name)
    obj.search_engine_url = data.get('search_engine_url', obj.search_engine_url)

    db.session.commit()
    return jsonify({"message": "Updated"})

@seosearch_bp.route('/seo-engine/<int:id>', methods=['PUT'])
def delete_seo_engine(id):
    obj = SEOSearchEngineModel.query.get(id)
    obj.is_deleted = True
    db.session.commit()
    return jsonify({"message": "Deleted"})