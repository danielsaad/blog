## Publicações

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      {% if post.except %}
          {{ post.excerpt }}
      {% endif %}
    </li>
  {% endfor %}
</ul>
