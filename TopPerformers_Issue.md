# ⚠️ Issue: FieldError in `top-performers` API

## 🔍 Problem
When calling the endpoint:
```
GET http://127.0.0.1:8000/api/students/top-performers/?limit=3
```
The server throws the following error:
```
django.core.exceptions.FieldError: Cannot resolve keyword 'test' into field. Choices are: department, email, id, name, tests
```

---

## 🧾 Root Cause
- In the `views.py` implementation of the `top_performers` method, the queryset filter was written as:
  ```python
  Student.objects.filter(test__isnull=False)
  ```
- However, in the **Test model**, the ForeignKey field is defined with `related_name="tests"`.  
- This means the reverse relation from `Student` → `Test` should be accessed as `tests`, not `test`.  


## 🧪 Testing
After fixing, call the endpoint again:
```
GET http://127.0.0.1:8000/api/students/top-performers/?limit=3
```
✅ The API should now return the top students with their average scores.

---

## 📌 Notes
- This issue was caused due to **incorrect related name usage** in Django ORM queries.  
- Always check the `related_name` defined in the model when querying reverse relations.  
