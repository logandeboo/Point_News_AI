import React, { Component }  from 'react';

export default function NewsItem({title, points, url, image_url, date, source}){
    return (
                <div className='news-item-body'>
                    <h3 className='item-title'>{title}</h3>
                    <div className="image-points-container">
                        <img className='news-img' src={image_url} alt={image_url} />
                        <div className="points-container">
                            <ul className="points">
                                <li>
                                    {points[0]}
                                </li>
                                
                                <li>
                                    {points[1]}
                                </li>
                                
                                <li>
                                    {points[2]}
                                </li>
                            </ul>
                        </div>
                    </div>
        <div className="citation"> Published by: <a href={url}>{source}</a> on {date}</div>
    </div>
)
}