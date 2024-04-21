// ImageUploader.js

import React, { useState } from 'react';
import axios from 'axios';
import Loader from '../loader/Loader';
import "./imageUpload.css";
import logo from "../../assets/logo.png";
import { toast, Toaster } from 'sonner'
import Markdown from 'react-markdown'


const ImageUploader = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [previewURL, setPreviewURL] = useState(null);
    const [geminiResponse, setGeminiResponse] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [isUploading, setIsUploading] = useState(false);

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (!file.type.startsWith('image/') && !file.name.endsWith('.tmp')) {
            toast('Please select an image file.');
            return;
        }
        setSelectedFile(file);
        setPreviewURL(URL.createObjectURL(file));
    };

    const handleUploadClick = async () => {
        setIsLoading(true);
        setIsUploading(true);
        console.log("Uploading image...");
        const formData = new FormData();
        formData.append('image', selectedFile);

        const uploadPromise = axios.post('http://localhost:5000/gemini', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });

        toast.promise(uploadPromise, {
            loading: 'Uploading image...',
            success: 'Image uploaded successfully!',
            error: 'Error uploading image',
        });

        try {
            const { data } = await uploadPromise;
            console.log("Image uploaded successfully!");

            // Wait for 1 seconds
            await new Promise(resolve => setTimeout(resolve, 1000));

            // Make a GET request to retrieve the Gemini response
            const response = await axios.get('http://localhost:5000/gemini', {
                params: {
                    image_path: data.image_path // Pass the image_path obtained from the POST request response
                }
            });
            console.log("Gemini response:", response.data.gemini_response);
            const result = response.data.gemini_response
            setGeminiResponse(result);
        } catch (error) {
            console.error('Error uploading image:', error);
        }
        setIsUploading(false);
        setIsLoading(false);
    };


    return (
        <div className="container">
            <Toaster richColors position="top-right" />
            <div className='heading'>
                <img src={logo} className='logo' alt="" />
            </div>
            <div className='content'>
                <div className='leftContent'>
                    {!previewURL && <input type="file" onChange={handleFileChange} className="file-input" />}
                    {previewURL && <img src={previewURL} alt="Preview" className="preview-image" />}
                    {!geminiResponse && !isUploading && <button onClick={handleUploadClick} className="upload-btn">Upload Image</button>}
                </div>
                <div className='rightContent'>
                    <span className='response'>
                        {isLoading ? <Loader /> : <Markdown>{geminiResponse}</Markdown>}
                    </span>
                </div>
            </div>
        </div>

    );
};

export default ImageUploader;