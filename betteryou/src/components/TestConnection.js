import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TestConnection = () => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get('http://localhost:8000/api/test-connection/')
            .then(response => {
                setMessage(response.data.message);
            })
            .catch(error => {
                console.error('There was an error!', error);
            });
    }, []);

    return (
        <div>
            <h1>Test Connection</h1>
            <p>{message}</p>
        </div>
    );
};

export default TestConnection;