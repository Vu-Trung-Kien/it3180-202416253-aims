def search_by_category(items, category):
    """Trả về các đĩa thuộc đúng thể loại."""
    return [dvd for dvd in items if dvd.category == category]


def search_by_title(items, keyword):
    """Trả về các đĩa có tiêu đề chứa keyword."""
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
