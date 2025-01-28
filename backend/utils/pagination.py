from flask import url_for

def build_pagination(page, per_page, total_items, total_pages, has_next, has_prev, next_num, prev_num):
    """
    Constrói o objeto de paginação com os links de navegação.
    """
    def build_pagination_links(page):
        return url_for('entity.get_entities', page=page, per_page=per_page, _external=True)

    next_page = build_pagination_links(next_num) if has_next else None
    prev_page = build_pagination_links(prev_num) if has_prev else None

    # Retorna o objeto de paginação
    return {
        "page": page,
        "per_page": per_page,
        "total_items": total_items,
        "total_pages": total_pages,
        "next_page": next_page,
        "prev_page": prev_page
    }