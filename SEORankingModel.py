from flask import Blueprint,request,jsonify 
from app import SEORankingModel

seoranking_bp = Blueprint("seoranking_bp",(__name__))






@seoranking_bp.route('/seo-ranking', methods=['POST'])
def create_seo_ranking():
    data = request.json
    obj = SEORankingModel(
        product_id=data['product_id'],
        vendor_id=data.get('vendor_id'),
        meta_title=data.get('meta_title'),
        meta_description=data.get('meta_description')
    )
    db.session.add(obj)
    db.session.commit()
    return jsonify(obj.to_dict())

@seoranking_bp.route('/seo-ranking', methods=['GET'])
def get_seo_ranking():
    data = SEORankingModel.query.filter_by(is_deleted=False).all()
    return jsonify([i.to_dict() for i in data])

@seoranking_bp.route('/seo-ranking/<int:id>', methods=['GET'])
def get_seo_ranking_by_id(id):
    obj = SEORankingModel.query.filter_by(id=id, is_deleted=False).first()
    return jsonify(obj.to_dict())

@seoranking_bp.route('/seo-ranking/<int:id>', methods=['PUT'])
def update_seo_ranking(id):
    data = request.json
    obj = SEORankingModel.query.get(id)

    obj.meta_title = data.get('meta_title', obj.meta_title)
    obj.meta_description = data.get('meta_description', obj.meta_description)

    db.session.commit()
    return jsonify(obj.to_dict())

@seoranking_bp.route('/seo-ranking/<int:id>', methods=['PUT'])
def delete_seo_ranking(id):
    obj = SEORankingModel.query.get(id)
    obj.is_deleted = True
    db.session.commit()
    return jsonify({"message": "Deleted"}) 
