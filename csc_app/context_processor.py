def global_context(request):
    return {
        "company": "Cuddalore",
        "user_ip": request.META.get("REMOTE_ADDR", "Unknown"),
    }
    
company = "Cuddalore"
site_pass = "607001"
uname = "cudcsc"