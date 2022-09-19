import NewsItem from './NewsItem'
import React, {useState, useEffect  }  from 'react';


export default function ItemFeed({topic}) {
    const [data, setData] = useState([]);
    useEffect(() => {
        // GET request using fetch inside useEffect React hook
        fetch(topic)
            .then(response => response.json())
            .then(data => {
                        
                        setData(data)
                        console.log(data)
                        
                      }
                    )
                  }, [topic])

    return (
        <div className='article-feed-container'> 
            {data.map(article => {
                return(
                    <NewsItem className='article-feed'
                        title={article.articleTitle}
                        points={article.articlePoints}
                        url={article.articleUrl}
                        image_url={article.articleImg}
                        date={article.articleDate}
                        source={article.articleSource.uri} 
                    />
                )
            })}
        </div>
    )
}

export { ItemFeed };




