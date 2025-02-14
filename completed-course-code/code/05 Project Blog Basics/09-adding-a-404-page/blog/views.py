from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "hiking-mountains-of-big-data",
        "image": "mountains.jpg",
        "author": "Lucas Thurston",
        "date": date(2021, 7, 21),
        "title": "Data Engineering",
        "excerpt": "One of the primary challenges in data engineering is managing data quality and ...",
        "content": """
          In today’s data-driven world, the ability to collect, process, and analyze vast amounts of information is crucial for making smarter decisions. At the heart of this process is data engineering—the backbone of modern data ecosystems. While data science often steals the spotlight, data engineering ensures that data is accessible, clean, and ready for analysis.
          
          Data engineering involves designing, building, and maintaining the infrastructure that enables data to flow efficiently from multiple sources to centralized systems like data warehouses and lakes. This process requires creating robust data pipelines that extract data from various systems, transform it into usable formats, and load it into target destinations. Technologies like Apache Spark, Airflow, and Kafka have become essential tools for building scalable pipelines.
          
          One of the primary challenges in data engineering is managing data quality and reliability. Raw data is often messy and inconsistent. Data engineers implement validation rules, deduplication processes, and monitoring systems to ensure that the data powering business decisions is accurate and up-to-date.
          
          In addition to managing structured data from relational databases, data engineers must handle unstructured data such as logs, videos, and social media feeds. Cloud platforms like AWS, Azure, and GCP have made it easier to build and scale infrastructure to manage these diverse data types.
          
          Data engineering is the foundation that enables businesses to harness the full potential of their data. Whether it's powering real-time analytics for personalized recommendations or supporting predictive models for financial forecasting, data engineers play a crucial role in turning raw data into actionable insights. In an era where data is king, data engineering is more essential than ever.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Lucas Thurston",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "cyber-landscape",
        "image": "woods.jpg",
        "author": "Lucas Thurston",
        "date": date(2020, 8, 5),
        "title": "Cybersecurity",
        "excerpt": "Cybersecurity is more than just a buzzword; it’s a multi-layered approach to protecting systems, networks, and ...",
        "content": """
          In an age where our lives are increasingly connected to the internet, cybersecurity has become more critical than ever. Cyber threats are evolving rapidly, targeting individuals, businesses, and governments alike. From data breaches to ransomware attacks, the consequences of weak security can be devastating—compromising sensitive information and disrupting essential services.
          
          Cybersecurity is more than just a buzzword; it’s a multi-layered approach to protecting systems, networks, and data. It involves securing devices, using encryption to protect communications, and implementing strong access controls. It also includes monitoring for threats and staying vigilant against social engineering tactics like phishing.
          
          The rise of the Internet of Things (IoT) and cloud computing has expanded the attack surface, making cybersecurity even more challenging. Organizations must adopt proactive strategies—such as regular security assessments and employee training—to stay ahead of threats. For individuals, simple steps like using strong, unique passwords and enabling two-factor authentication can significantly reduce risk.
          
          Ultimately, cybersecurity is everyone’s responsibility. Whether you’re a business leader or an everyday user, understanding the basics and adopting good practices can help create a safer digital environment for all.
          
          In today’s interconnected world, cybersecurity has become one of the most critical fields. As our reliance on technology grows, so does the risk of cyber threats, ranging from data breaches to sophisticated ransomware attacks. Cybersecurity isn't just about protecting systems—it's about safeguarding the data, privacy, and trust of individuals and organizations.
          
          The foundation of cybersecurity lies in three core principles: confidentiality, ensuring sensitive information is accessed only by authorized users; integrity, maintaining the accuracy and reliability of data; and availability, ensuring systems and data are accessible when needed. These principles guide cybersecurity strategies across industries, from financial services to healthcare.
          
          Threat actors are continuously evolving, employing phishing, social engineering, and advanced persistent threats to exploit vulnerabilities. To counter this, companies must adopt a proactive approach—combining robust encryption, network monitoring, and employee training. Additionally, frameworks like Zero Trust Architecture emphasize verifying every user and device before granting access, ensuring an extra layer of defense.
          
          Cybersecurity is not just the responsibility of IT professionals. Whether it’s creating strong passwords, avoiding suspicious links, or keeping software updated, everyone has a role to play. As threats continue to grow in complexity, fostering a culture of security awareness is more critical than ever.
          
          In a world where data is the new currency, protecting it is no longer optional—it’s a necessity. Cybersecurity is the key to ensuring trust and resilience in our digital future.
        """
    }
]

def get_date(post):
  return post['date']

# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
      "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
      "post": identified_post
    })
