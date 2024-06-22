import React, { useState } from 'react';

function CustomContent() {
    const [description, setDescription] = useState('');

    const handleInputChange = (event) => {
        setDescription(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch('/api/generate-code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ description }),
        });
        const data = await response.json();
        console.log(data.code);
    };

    return (
        <div>
            <h1>Custom Content</h1>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={description}
                    onChange={handleInputChange}
                    placeholder="Describe your custom content..."
                />
                <button type="submit">Generate Code</button>
            </form>
        </div>
    );
}

export default CustomContent;