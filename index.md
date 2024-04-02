## Publicações

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | prepend:site.baseurl }}">{{ post.title }} -- <i> {{ post.date | date: "%d/%m/%Y"  }} </i> </a>
      {% if post.except %}
          {{ post.excerpt }}
      {% endif %}
    </li>
  {% endfor %}
</ul>
