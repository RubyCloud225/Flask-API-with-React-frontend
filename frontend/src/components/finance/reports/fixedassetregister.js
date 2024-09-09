import React, { useState } from 'react';

function FixedAssetRegister() {
    const [assetId, setAssetId] = useState("");
    const [assetName, setAssetName] = useState("");
    const [assetCost, setAssetCost] = useState("");
    const [assetLocation, setAssetLocation] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('/fixedasset', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    assetId,
                    assetName,
                    assetCost,
                    assetLocation
                })
            });
            const data = await response.json();
            console.log(data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <h1>Fixed Asset Register</h1>
            <form onSubmit={handleSubmit}>
                <label>Asset ID:
                    <input type="text" value={assetId} onChange={(e) => setAssetId(e.target.value)} /></label>
                <br />
                <label>Asset Name:
                    <input type="text" value={assetName} onChange={(e) => setAssetName(e.target.value)} /></label>
                <br />
                <label>Asset Cost:
                    <input type="number" value={assetCost} onChange={(e) => setAssetCost(e.target.value)} /></label>
                <br />
                <label>Asset Location:
                    <select value={assetLocation} onChange={(e) => setAssetLocation(e.target.value)} /></label>
                <br />
                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

export default FixedAssetRegister;