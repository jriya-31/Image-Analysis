import React, { useState, useEffect } from "react";

const OCRDataEditor = ({ userId }) => {
    const [data, setData] = useState(null);
    const [editedData, setEditedData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch data from the backend
    useEffect(() => {
        fetch(`/api/get-data/${userId}/`)
            .then((response) => response.json())
            .then((result) => {
                setData(result);
                setEditedData(result); // Set for editing
                setLoading(false);
            })
            .catch((error) => {
                setError("Failed to fetch data");
                setLoading(false);
            });
    }, [userId]);

    // Handle input changes
    const handleChange = (e, key) => {
        setEditedData((prevData) => ({
            ...prevData,
            documents: {
                ...prevData.documents,
                [key]: e.target.value
            }
        }));
    };

    // Save updated data
    const handleSave = () => {
        fetch("/api/save-data/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                user_id: userId,
                documents: editedData.documents
            }),
        })
            .then((response) => response.json())
            .then((result) => {
                alert("Data saved successfully!");
            })
            .catch((error) => {
                alert("Error saving data.");
            });
    };

    if (loading) return <p>Loading...</p>;
    if (error) return <p>{error}</p>;

    return (
        <div>
            <h2>Extracted OCR Data</h2>
            {Object.keys(data.documents).map((key) => (
                <div key={key}>
                    <label>{key}: </label>
                    <input
                        type="text"
                        value={editedData.documents[key]}
                        onChange={(e) => handleChange(e, key)}
                    />
                </div>
            ))}
            <button onClick={handleSave}>Save</button>
        </div>
    );
};

export default OCRDataEditor;
