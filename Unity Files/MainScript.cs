using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;

public class MainScript : MonoBehaviour
{
    //public prefab object
    public GameObject particlePrefab;
    public int systemWidth;
    public int particleAmount;
    public float maxStepDistance;
    public int spatialHashGridSize;
    // Start is called before the first frame update
    private bool autoRun = false;
    Dictionary<Vector3Int, List<GameObject>> spatialHash = new Dictionary<Vector3Int, List<GameObject>>();

    void Start()
    {
        //set the size of the square called background to the system width
        GameObject.Find("Background").transform.localScale = new Vector3(systemWidth, systemWidth, 1);
        
        //set the orthographic size of the camera to the system width
        GameObject.Find("Main Camera").GetComponent<Camera>().orthographicSize = systemWidth/2;
        
        //create a square grid of particleAmount particles
        int sideLength = (int)Mathf.Sqrt(particleAmount);

        for (int i = -(int)sideLength/2; i < (int)sideLength/2; i++)
        {
            for (int j = -(int)sideLength/2; j < (int)sideLength/2; j++)
            {
                //instantiate a particle prefab
                GameObject particle = Instantiate(particlePrefab);
                //set the position of the particle to the correct position in the grid
                particle.transform.position = new Vector3(i * systemWidth / sideLength, j * systemWidth / sideLength, 0);
                //set the parent of the particle to the particle system
                particle.transform.parent = GameObject.Find("Particle System").transform;
            }
        }
        initAllParticlesInSpatialHash();
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.R))
        {
            autoRun = !autoRun;
        }

        //if the spacebar is pressed, call the function moveParticles

        if (Input.GetKeyDown(KeyCode.Space) || autoRun)
        {
            moveParticles();
        }
            
    }

    void initAllParticlesInSpatialHash() {
        GameObject particleSystem = GameObject.Find("Particle System");
        foreach(Transform child in particleSystem.transform)
        {
            Vector3Int index = spatialHashIndex(child.transform.position);
            if(!spatialHash.ContainsKey(index)) {
                spatialHash.Add(index, new List<GameObject>());
            }
            spatialHash[index].Add(child.transform.gameObject);
        }
    }

    void moveParticles() {
        GameObject particleSystem = GameObject.Find("Particle System");
        float spatialHashGridSquareSize = systemWidth / spatialHashGridSize;

        foreach(Transform child in particleSystem.transform)
        {
            Vector3 originalPosition = child.transform.position;
            Vector3Int originalSpatialHashIndex = spatialHashIndex(originalPosition);
            spatialHash[originalSpatialHashIndex].Remove(child.transform.gameObject);

            child.transform.position += new Vector3(UnityEngine.Random.Range(-maxStepDistance, maxStepDistance), UnityEngine.Random.Range(-maxStepDistance, maxStepDistance), 0);
            
            Vector3Int newSpatialHashIndex = spatialHashIndex(child.transform.position);
            Vector3Int[] vectorsForSorroundingCells = {new Vector3Int(-1, 1, 0), new Vector3Int(-1, 0, 0), new Vector3Int(-1, -1, 0), new Vector3Int(0, 1, 0), new Vector3Int(0, 0, 0), new Vector3Int(0, -1, 0), new Vector3Int(1, 1, 0), new Vector3Int(1, 0, 0), new Vector3Int(1, -1, 0)};
            
            float x = child.transform.position.x;
            float y = child.transform.position.y;

            if(y < -systemWidth/2) {
                child.transform.position = new Vector3(x, systemWidth/2, 0);
            }
            if(y > systemWidth/2) {
                child.transform.position = new Vector3(x, -systemWidth/2, 0);
            }
            if(x < -systemWidth/2 || x > systemWidth/2) {
                child.transform.position = originalPosition;
            }

            foreach(Vector3Int neighborVector in vectorsForSorroundingCells) {
                if(!spatialHash.ContainsKey(newSpatialHashIndex + neighborVector)) {
                    spatialHash.Add(newSpatialHashIndex + neighborVector, new List<GameObject>());
                }
                foreach(GameObject neighbor in spatialHash[newSpatialHashIndex + neighborVector]) {

                    if (Vector3.Distance(child.transform.position, neighbor.transform.position) < 1) {
                        child.transform.position = originalPosition;
                    }
                }
            }
            spatialHash[spatialHashIndex(child.transform.position)].Add(child.transform.gameObject);
        }
    }

    Vector3Int spatialHashIndex(Vector3 position)
    {
        float spatialHashGridSquareSize = systemWidth / spatialHashGridSize;
        return Vector3Int.FloorToInt(position / spatialHashGridSquareSize);
    }
}
