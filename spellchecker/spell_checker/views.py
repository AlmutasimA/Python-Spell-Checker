from django.shortcuts import render, JsonResponse
from .models import DictionaryWord
from spell_checker import spell_checker

def suggest_corrections(request):
  if request.method == "POST":
    word = request.POST.get("word")
    if word:
      dictionary = list(DictionaryWord.objects.values_list("word", flat=True))
      suggestions = spell_checker(word, dictionary)
      return JsonResponse({"suggestions": suggestions})
  return JsonResponse({"error": "Invalid request"})

# Additional view to add words to the dictionary (optional)
def add_to_dictionary(request):
  if request.method == "POST":
    word = request.POST.get("word")
    if word and word not in DictionaryWord.objects.values_list("word", flat=True):
      DictionaryWord.objects.create(word=word)
      return JsonResponse({"success": True})
  return JsonResponse({"error": "Invalid request"})