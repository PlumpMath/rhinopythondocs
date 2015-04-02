### missing modules (1)  
  - math

### total missing methods (445)  

#### application (30)
  - 30 missing in application.py
    - AddStartupScript
    - AppearanceDisplay
    - DeleteStartupScript
    - EnableHistoryRecording
    - Help
    - LastLoadedScriptFile
    - PlugInIds
    - PlugInName
    - PlugInInfo
    - Print
    - RegistryKey
    - StartupScriptCount
    - StartupScriptList
    - StatusBarNumber
    - SdkServiceRelease
    - SerialNumber
    - NodeType
    - InstallType
    - StatusBarProgressMeter
    - SnapToLocked
    - ShowIsocurves
    - IsocurveDensity
    - UPlaneMode
    - CommandLineArgs
    - CheckNewObjects
    - WorkSessionFileName
    - WorkSessionModelCount
    - WorkSessionModelNames
    - WorkSessionModelAliases
    - RecentFiles
  + 4 extras in application.py
    + IsRunningOnWindows
    + StatusBarProgressMeterShow
    + StatusBarProgressMeterUpdate
    + StatusBarProgressMeterHide

#### curve (25)
  - 25 missing in curve.py
    - AddCirclePtTanPt
    - AddInterpCurveEx
    - CurveEvaluate
    - EllipseFocalDistance
    - EllipseFoci
    - IsNurbsCurve
    - MakeCurvePeriodic
    - RemoveCurveKnot
    - OffsetCurveNormal
    - ExtractPolyCurveSegment
    - LineCurveIntersection
    - PlaneCurveIntersection
    - IsEllipticalArc
    - ConvertCurveToBezier
    - AddPolygon
    - AddStarPolygon
    - FilletCurves
    - RemoveShortCurveSegments
    - TweenCurve
    - AddSpiral2
    - CurveRailFrames
    - SmoothCurve
    - AddTextOutlines
    - CleanUpPolyCurve
    - ChangeCurveDegree
  + 2 extras in curve.py
    + AddRectangle
    + LineFitFromPoints

#### document (13)
  - 13 missing in document.py
    - DocumentURL
    - RenderMeshDensity
    - RenderMeshMaxAngle
    - RenderMeshMaxAspectRatio
    - RenderMeshMaxDistEdgeToSrf
    - RenderMeshMaxEdgeLength
    - RenderMeshMinEdgeLength
    - RenderMeshMinInitialGridQuads
    - RenderMeshQuality
    - RenderMeshSettings
    - UnitCustomUnitSystem
    - UnitDistanceDisplayMode
    - DocumentInfo

#### geometry (112)
  - 112 missing in geometry.py
    - FlipClippingPlane
    - ClippingPlaneDefinition
    - TextObjectJustification
    - TextObjectFormula
    - TextDotStyle
    - LineLineIntersection
    - LinePlaneIntersection
    - IntersectPlanes
    - PlanePlaneIntersection
    - LineCylinderIntersection
    - LineSphereIntersection
    - PlaneSphereIntersection
    - IntersectSpheres
    - ProjectPointToMesh
    - ProjectPointToSurface
    - PullPoints
    - LineClosestPoint
    - LineFitFromPoints
    - LineIsFartherThan
    - LineMaxDistanceTo
    - LineMinDistanceTo
    - LinePlane
    - LineTransform
    - DistanceToPlane
    - EvaluatePlane
    - MovePlane
    - PlaneClosestPoint
    - PlaneEquation
    - PlaneFitFromPoints
    - PlaneFromFrame
    - PlaneFromNormal
    - PlaneFromPoints
    - PlaneTransform
    - RotatePlane
    - WorldXYPlane
    - WorldYZPlane
    - WorldZXPlane
    - PlaneAngle
    - PointAdd
    - PointCompare
    - PointDivide
    - PointsAreCoplanar
    - PointScale
    - PointSubtract
    - PointTransform
    - PointArrayBoundingBox
    - PointArrayClosestPoint
    - PointArrayTransform
    - IsVectorParallelTo
    - IsVectorPerpendicularTo
    - IsVectorTiny
    - IsVectorZero
    - VectorAdd
    - VectorAngle
    - VectorCompare
    - VectorCreate
    - VectorCrossProduct
    - VectorDivide
    - VectorDotProduct
    - VectorLength
    - VectorMultiply
    - VectorReverse
    - VectorRotate
    - VectorScale
    - VectorSubtract
    - VectorTransform
    - VectorUnitize
    - IsXformIdentity
    - IsXformSimilarity
    - IsXformZero
    - XformChangeBasis
    - XformCompare
    - XformCPlaneToWorld
    - XformDeterminant
    - XformDiagonal
    - XformIdentity
    - XformInverse
    - XformMirror
    - XformMultiply
    - XformPlanarProjection
    - XformRotation
    - XformScale
    - XformScreenToWorld
    - XformShear
    - XformTranslation
    - XformWorldToCPlane
    - XformWorldToScreen
    - XformZero
    - IsXformSingular
    - XFormWorldToLayout
    - XFormLayoutToWorld
    - CompareGeometry
    - E
    - PI
    - Polar
    - ToDegrees
    - ToRadians
    - LineBoxIntersection
    - LineCircleIntersection
    - LineArcIntersection
    - PlaneCircleIntersection
    - PlaneArcIntersection
    - PointClosestObject
    - IsPictureFrame
    - CircleFromPoints
    - LineBetweenCurves
    - IsKnotVectorClamped
    - IsKnotVectorPeriodic
    - IsKnotVectorUniform
    - KnotVectorHasBezierSpans
    - KnotVectorStyle
    - CircleCircleIntersection
  + 2 extras in geometry.py
    + Area
    + ExplodeText

#### group (3)
  - 3 missing in group.py
    - RemoveObjectFromTopGroup
    - GetGroupUserText
    - SetGroupUserText

#### userinterface (14)
  - 14 missing in userinterface.py
    - GetAngleEx
    - HtmlBox
    - IntegerBox
    - MessageBeep
    - GetLinetype
    - GetPrintWidth
    - GetSurfaceIsoParamPoint
    - GetPointOnPlane
    - GetPointOnLine
    - GetPolyline
    - EditListBox
    - OrderListBox
    - GetCircle
    - GetOption
  + 3 extras in userinterface.py
    + FilterById
    + CustomGeometryFilter
    + GetPointDynamicDrawFunc

#### layer (6)
  - 6 missing in layer.py
    - LayerMode
    - LayerMaterialId
    - MatchLayer
    - MergeLayer
    - GetLayerUserText
    - SetLayerUserText

#### material (10)
  - 10 missing in material.py
    - ObjectsByMaterialIndex
    - ObjectsByMaterialSource
    - MaterialCount
    - MaterialsByColor
    - MaterialsByName
    - MaterialIds
    - MaterialId
    - MaterialIndex
    - IsMaterial
    - MaterialIndices

#### object (53)
  - 53 missing in object.py
    - AddObjectMesh
    - ObjectNames
    - ObjectTopGroup
    - ObjectURL
    - OrientObjects
    - RemapObject
    - RemapObjects
    - ZoomObject
    - ZoomObjects
    - ObjectGripsOn
    - ObjectGripsSelected
    - EnableObjectGrips
    - ObjectGripCount
    - SelectObjectGrip
    - SelectObjectGrips
    - UnselectObjectGrip
    - UnselectObjectGrips
    - ObjectGripLocation
    - ObjectGripLocations
    - NextObjectGrip
    - PrevObjectGrip
    - SelectedObjectGrips
    - GetObjectGrip
    - GetObjectGrips
    - ObjectDump
    - ObjectHasMesh
    - EnableObjectMesh
    - ObjectMeshQuality
    - ObjectMeshDensity
    - ObjectMeshMaxAngle
    - ObjectMeshMaxAspectRatio
    - ObjectMeshMinEdgeLength
    - ObjectMeshMaxEdgeLength
    - ObjectMeshMaxDistEdgeToSrf
    - ObjectMeshMinInitialGridQuads
    - ObjectMeshSettings
    - DeleteObjectMesh
    - BoxMorphObject
    - ObjectGripOwner
    - AddObjectDisplayMode
    - ObjectDisplayMode
    - RemoveObjectDisplayMode
    - ObjectClash
    - ReplaceGeometry
    - ObjectHasHistory
    - ObjectParents
    - ObjectChildren
    - IsObjectParent
    - IsObjectChild
    - ChangeObjectSpace
    - ObjectSpace
    - ObjectSerialNumber
    - ObjectDataCRC

#### selection (7)
  - 7 missing in selection.py
    - ReferenceObjects
    - ObjectsByURL
    - UnselectedObjects
    - PrevSelectedObjects
    - PointPick
    - ObjectsByRegion
    - FilterObjects
  + 4 extras in selection.py
    + CustomGeometryFilter
    + GetObjectEx
    + GetObjects
    + GetObjectsEx

#### surface (42)
  - 42 missing in surface.py
    - IsPolySurface
    - IsPolySurfaceClosed
    - IsPolySurfacePlanar
    - SurfaceContourPoints
    - ExplodePolySurfaces
    - SurfaceSurfaceIntersection
    - JoinSurfacesEx
    - InsertSurfaceKnot
    - AddRailRevSrf
    - SurfaceCurvatureAnalysis
    - SurfacePrincipalCurvature
    - AddSrfSectionCrvs
    - SurfaceSeam
    - FitSurface
    - IsBrepManifold
    - IsParameterOnSurface
    - SurfaceSphere
    - ExtrudeCurveTapered
    - RemoveSurfaceKnot
    - MakeSurfaceNonPeriodic
    - CreateSolid
    - IsBox
    - BoxPoints
    - SurfaceDraftAnglePoint
    - IsExtrusion
    - SplitSurface
    - ExtrudeCurveNormal
    - ConvertSurfaceToBezier
    - SurfaceCount
    - AddNetworkSrfEx
    - AddThickPipe
    - IsSurfaceUnrollable
    - Add1RailSweep
    - Add2RailSweep
    - AddExtrusion
    - AddTruncatedCone
    - OffsetBrep
    - ConvertExtrusion
    - SmoothSurface
    - SplitSurfaceEx
    - MergeSurfaces
    - ChangeSurfaceDegree
  + 4 extras in surface.py
    + ExplodePolysurfaces
    + IntersectSpheres
    + IsPolysurface
    + IsPolysurfaceClosed

#### toolbar (13)
  - 13 missing in toolbar.py
    - ToolbarCollectionName
    - ToolbarCollectionAlias
    - ToolBarCount
    - ToolBarNames
    - ToolBarAlias
    - IsToolBar
    - ShowToolBar
    - HideToolBar
    - IsToolBarVisible
    - AddToolbarCollection
    - AddToolBar
    - DeleteToolBar
    - AddToolBarButton
  + 6 extras in toolbar.py
    + HideToolbar
    + IsToolbar
    + IsToolbarVisible
    + ShowToolbar
    + ToolbarCount
    + ToolbarNames

#### userdata (14)
  - 14 missing in userdata.py
    - GetObjectData
    - SetObjectData
    - DeleteObjectData
    - ObjectDataCount
    - IsObjectData
    - GetAttributeData
    - SetAttributeData
    - DeleteAttributeData
    - AttributeDataCount
    - IsAttributeData
    - IsDocumentUserText
    - GetRuntimeData
    - SetRuntimeData
    - RuntimeDataCount

#### utility (29)
  - 29 missing in utility.py
    - Version
    - SaveSettings
    - IsProcedure
    - AllProcedures
    - Pt2Str
    - Str2PtArray
    - Strtok
    - CurrentPrinter
    - PrinterNames
    - SpoolToPrinter
    - JoinArrays
    - SortPointsEx
    - CullDuplicateStrings
    - SortStrings
    - SortNumbers
    - FindDuplicateStrings
    - FindDuplicateNumbers
    - FindDuplicatePoints
    - TextOut
    - MakeArray
    - ColorRGBToHSV
    - ColorHSVToRGB
    - ReadDelimitedFile
    - ReadTextFile
    - SortPointsByDistance
    - WriteTextFile
    - ImageInfo
    - UnionStrings
    - IntersectStrings
  + 6 extras in utility.py
    + ContextIsRhino
    + ContextIsGrasshopper
    + Angle
    + Angle2
    + Distance
    + Polar

#### view (13)
  - 13 missing in view.py
    - SynchronizeCPlanes
    - DetailNames
    - IsBackgroundBitmap
    - BackgroundBitmap
    - ViewDisplayModeEx
    - DeleteViewDisplayMode
    - ExportViewDisplayMode
    - ImportViewDisplayMode
    - IsViewOutOfPlan
    - ViewCameraIcon
    - ViewXform
    - ViewProjectionXform
    - ViewFlatShade
  + 4 extras in view.py
    + AddDetail
    + AddLayout
    + DetailLock
    + DetailScale

#### block (3)
  - 3 missing in block.py
    - BlockURL
    - BlockURLTag
    - IsBlockObject
  + 1 extras in block.py
    + InsertBlock2

#### dimension (8)
  - 8 missing in dimension.py
    - DimScale
    - DimStyleScale
    - AddRadialDimension
    - DimStyleDimLineExtension
    - DimStyleCentermarkSize
    - IsDimStyleChild
    - ParentDimStyle
    - DimStyleFieldOverride

#### mesh (24)
  - 24 missing in mesh.py
    - MeshContourPoints
    - MeshTextureCoordinates
    - MeshHasHiddenVertices
    - MeshHideVertices
    - LineMeshIntersection
    - MeshObjects
    - MeshParameters
    - MeshParameterDensity
    - ReduceMesh
    - ExtractRenderMesh
    - ExtractAnalysisMesh
    - MeshPlaneIntersection
    - ConnectedMeshFaces
    - MeshPart
    - FlipMesh
    - WeldMesh
    - UnweldMesh
    - DeleteMeshFace
    - IsMeshDoublePrecision
    - MeshAreaMoments
    - MeshVolumeMoments
    - SmoothMesh
    - MeshPatch
    - ExtractMeshHelper

#### math (24)
  - 24 missing in math.py
    - ACos
    - ACosH
    - Angle
    - Angle2
    - ASin
    - ASinH
    - ATan2
    - ATanH
    - Ceil
    - CosH
    - Deviation
    - Distance
    - Floor
    - Hypot
    - Log10
    - Max
    - Mean
    - Median
    - Min
    - SinH
    - SolveQuadratic
    - Sum
    - TanH
    - Rnd

#### hatch (2)
  - 2 missing in hatch.py
    - DuplicateHatchBorders
    - HatchArea
