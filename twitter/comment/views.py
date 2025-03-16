from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import CommentForm
from .models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class SendComment(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        form = CommentForm()
        query = request.GET.get('t')
        if query:
            comments = Comment.objects.filter(Q(writer__icontains=query)|Q(itself__icontains=query))
        else:
            comments = Comment.objects.all()
        return render(request, 'chat.html', {'form': form, 'comments': comments})
    
    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = request.user.username
            comment.save()
            return redirect('sendcomment')
        query = request.GET.get('t')
        if query:
            comments = Comment.objects.filter(Q(writer__icontains=query)|Q(itself__icontains=query))
        else:
            comments = Comment.objects.all()
        return render(request, 'chat.html', {'form': form, 'comments': comments})
    


class EditComment(View):
    def get(self, r, pk):
        comment = get_object_or_404(Comment, pk=pk)
        form = CommentForm(instance=comment)
        return render(r, 'editcomment.html', {'form': form, 'comment': comment})

    def post(self, r, pk):
        comment = get_object_or_404(Comment, pk=pk)
        form = CommentForm(r.POST, r.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('sendcomment')
        return render(r, 'editcomment.html', {'form': form, 'comment': comment})
    
class DeleteComment(View):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        return render(request, 'deletecomment.html', {'comment': comment})

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return redirect('sendcomment')